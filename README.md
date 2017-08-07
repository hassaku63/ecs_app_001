# ECS Sample App
Simple web app

# はじめに
ECS検証用に簡単なSlack連携のアプリケーションを書きました。
/hello にアクセスがあるとSlackにポストを実行するだけの作りになってます。

# ローカル実行
`git clone` した後、dockerインストール済みのマシンで以下を実行します。

実行するユーザーには予めdocker実行権限を持つグループを付与してください。

```bash
cd ecs_sampleapp
docker build -t ecs_sampleapp .
docker run -d --name=app -p 80:8080 -e SLACK_WEBHOOK_URL=<YOUR_SLACK_WEBHOOK_URL> ecs_sampleapp
```

# 注意事項

## 動作要件
SLACK_WEBHOOK_URL が環境変数として正しくセットされていることを期待して動作します。

## ECSデプロイ時の注意
このコードはDockerインストール済みのマシン、あるいはECS上で稼働することを想定したものですが、ECSにデプロイする場合は動作検証以上の目的では利用しないでください。

SlackのWebhook URLは、URLを知っていれば誰でもそのWebhookを利用できてしまいます。
ECSにもコンテナに環境変数を持たせる仕組みがあるものの、ReadOnlyの権限があればそのURLは取得できてしまうため、
センシティブな情報を持たせる場所としては適していません。
その目的には別のサービスを利用するようにします。後日その記事も記載できればと思います。
