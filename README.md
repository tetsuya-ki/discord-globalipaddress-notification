
# このBotについて

- `$ip`をDiscordに投稿すると、Botが起動しているサーバーのグローバルIPアドレスをDiscordにWebhookで通知します。
- ![image](https://github.com/tetsuya-ki/images/blob/main/discord-globalipaddress-notification/ipcommand.png?raw=true)

## 環境構築について

### 前提

1. pythonの3系がインストールされていること
   1. raspberry piの場合最初から入っているらしい
2. gitがインストールされていること
   1. raspberry piの場合、`sudo apt-get install -y git`でOK
   2. 使う分には公開鍵の登録等は不要
3. Discordの管理者（もしくは、Webhookを作成してもらえる立場）であること

### 前準備

1. GitHubから`git clone`する
   1. `git clone https://github.com/tetsuya-ki/discord-globalipaddress-notification.git`
   2. `cd discord-globalipaddress-notification`し、実行ディレクトリにカレントディレクトリを変更しておく
2. discordの開発者サイトに行き、Botを作成する
   1. こちらのサイトを参照: <https://discordpy.readthedocs.io/ja/latest/discord.html>
   2. 権限は`send messages`のみでOK
3. DiscordのギルドにBotを登録する
   1. 招待リンクを作成し、それをクリックすると招待画面に行くので目的のギルドに登録する
   2. Botの追加はサーバー管理者ロールを保持している必要アリ(権限がない場合、ダイアログにギルドが表示されない、かも)
4. DiscordのWebhookを作成し、保管しておく
   1. Discordの管理者の場合、投稿先のチャンネルで「チャンネルの編集」をクリック
   2. 「連携サービス」をクリック
   3. 「ウェブフック」をクリック
   4. 「新しいウェブフック」をクリックし、作成できる

### 準備

1. 必要な情報を保管する、`.env`ファイルを作成
   1. `.env.sample`をコピーし、名前を`.env`にする
   2. `.env`の「DISCORD_TOKEN_IS_HERE」に、**Botのトークンを入力する**
   3. `.env`の「WEBHOOK_IS_HERE」に、**DiscordのWEBHOOKのURLを入力**し、保存する
2. pythonの仮想環境を作成
   1. python3 -m venv venv
   2. source venv/bin/activate
3. 必要なパッケージを`requirements.txt`からインストール
   1. `pip install -r requirements.txt`

### Botの起動/停止

- `python bot.py`で起動する(We have logged in as xxxと記載されたら起動成功)

```sh
(venv) MacBookPro:discord-globalipaddress-notification name$ python bot.py
WARNING:discord.client:PyNaCl is not installed, voice will NOT be supported
INFO:discord.client:logging in using static token
...（中略）...
INFO:__main__:We have logged in as <あなたのBotのお名前>
```

- `Ctrl + C`で停止
