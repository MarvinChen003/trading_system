import tushare as ts
import requests
import json


TOKEN="PLEASE_USE_YOUR_OWN_TOKEN_TO_TUSHARE"
URL="http://api.tushare.pro"
API_NAME="daily"


def call_api():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "ts_code": "603506.SH",
            "start_date": "20190512",
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




