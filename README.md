# ECS App 001
Simple web app working on Amazon ECS

# docker run (local machine)

Clone this repository, then run following command

```bash
cd ecs_app_001
docker build -t ecsapp .
docker run -d --name=app001 -p 80:8080 -e SLACK_WEBHOOK_URL=<YOUR_SLACK_WEBHOOK_URL> ecsapp
```


