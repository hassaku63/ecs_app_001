# ECS App 001
Simple web app

# はじめに
動作検証に利用するdocker iamgeの元になるセットを書いたものです。
このレポジトリ自体はECSと無関係なので、あしからず。

http://blog.serverworks.co.jp/tech/2017/06/18/deploying_app_to_ecs/

※2017/06/19時点では非公開

# ローカルで実行
`git clone` した後、dockerインストール済みのマシンで以下を実行します。

実行するユーザーには予めdocker実行権限を持つグループを付与してください。

```bash
cd ecs_app_001
docker build -t ecs_app_001 .
docker run -d --name=app -p 80:8080 -e SLACK_WEBHOOK_URL=<YOUR_SLACK_WEBHOOK_URL> ecs_app_001
```

# 注意事項

## 動作要件
SLACK_WEBHOOK_URL が環境変数として正しくセットされていることを期待して動作します。

## ECSデプロイ時の注意
このコードはECS上で稼働することを想定したものですが、ECSにデプロイする場合は動作検証以上の目的では利用しないでください。

SlackのWebhook URLは、URLを知っていれば誰でもそのWebhookを利用できてしまいます。
ECSにもコンテナに環境変数を持たせる仕組みがあるものの、ReadOnlyの権限があればそのURLは取得できてしまうため、
センシティブな情報を持たせる場所としては適していません。
その目的には別のサービスを利用するようにしましょう。

※後日のブログで紹介予定です。
