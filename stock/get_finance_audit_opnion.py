# 获取财务审计意见

import os
import tushare as ts
import requests
import json


TOKEN = os.environ.get('TUSHARE_TOKEN')
URL = "http://api.tushare.pro"
API_NAME = "fina_audit"


def call_api():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "ts_code": "603506.SH",
            "start_date": "20100512",
            "end_date": "20200513",
        }
    }

    headers = {
        "Accept": "application/json",
    }

    r = requests.post(
        URL,
        data=json.dumps(payload),
        headers=headers,
    )

    print(r.json())
    return r.json()


if __name__ == "__main__":
    call_api()