#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import requests
import json
from urllib.parse import urlencode
from bottle import route, run

# define slack constants
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
headers = {"Content-Type": "application/x-www-form-urlencoded"}
param = dict(text="test massage")
param = "payload={dumped_dict}".format(dumped_dict=json.dumps(param))

@route('/hello')
def index():
  resp = requests.post(WEBHOOK_URL, data=param, headers=headers)
  return "<b>hello, Amazon ECS</b>!"

run(host="0.0.0.0", port=8080)
