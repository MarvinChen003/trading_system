import tushare as ts
import requests
import json


TOKEN="ea4fe281f13430950e3d7ad661af222ee5543e48d46198995693567d"
URL="http://api.tushare.pro"
API_NAME="daily"


def call_api():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "ts_code": "600233.SH",
            "start_date": "20200512",
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




