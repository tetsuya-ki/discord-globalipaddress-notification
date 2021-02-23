from discord import Webhook, AsyncWebhookAdapter
from logging import basicConfig, getLogger, INFO

import discord, aiohttp
import readenv

basicConfig(level=INFO)
LOG = getLogger(__name__)
GLOBAL_IP_ADDRESS_URL='http://httpbin.org/ip' # グローバルIPを教えてくれるサイト(jsonで返す)

client = discord.Client()

@client.event
async def on_ready():
    LOG.info('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Bot自身は無視(無限ループ回避のため)
    if message.author == client.user:
        return

    # 「$ip」と入力されたときにだけ反応する
    if message.content.startswith('$ip'):
        global_ip_address = ''
        async with aiohttp.ClientSession() as session:
            async with session.get(GLOBAL_IP_ADDRESS_URL) as response:
                LOG.info(GLOBAL_IP_ADDRESS_URL)
                if response.status != 200:
                    error_message = 'グローバルIPアドレスを教えてくれるサイトのURLが不正なので実行できません。'
                    LOG.error(error_message)
                else:
                    json = await response.json()
                    global_ip_address = json['origin'] # json形式で返却されるので、そこからIPアドレスを取り出す{"origin": "x.x.x.x"}
        if len(readenv.WEBHOOK_URL) > 0:
            # 予めWebhookが有効(HTTP_STATUSが200)か確認
            async with aiohttp.ClientSession() as session:
                async with session.get(readenv.WEBHOOK_URL) as r:
                    LOG.info(readenv.WEBHOOK_URL)
                    if r.status != 200:
                        error_message = 'Webhookが不正なので実行できません。'
                        LOG.error(error_message)
                    else:
                        # webhookを使って投稿する処理
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(readenv.WEBHOOK_URL, adapter=AsyncWebhookAdapter(session))
                            try:
                                # 投稿する
                                await webhook.send(f'あなたのグローバルIPアドレスはコチラです: {global_ip_address}', username='nofification_your_global_ipaddress')
                            except (discord.HTTPException,discord.NotFound,discord.Forbidden,discord.InvalidArgument) as e:
                                LOG.error(e)

# Botを起動
client.run(readenv.DISCORD_TOKEN)