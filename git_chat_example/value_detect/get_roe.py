from recommend_pool_20200712 import RECOMMEND_POOL

import tushare as ts
import requests
import json
import pandas as pd
import time


TOKEN = "YOUR_TOKEN"
URL = "http://api.tushare.pro"


def _get_roe_payload(stock_code):
    return {
        "api_name": "fina_indicator",
        "token": TOKEN,
        "params": {"ts_code": stock_code,},
    }


def _call_api(payload):

    payload

    headers = {
        "Accept": "application/json",
    }

    r = requests.post(URL, data=json.dumps(payload), headers=headers,)

    return r.json()


def _covert_json_to_pandas_dataframe(json_data):
    fields = json_data["data"]["fields"]
    items = json_data["data"]["items"]
    dafaframe = pd.DataFrame(columns=fields, data=items)
    return dafaframe


if __name__ == "__main__":

    stock_roe_higer_than_20 = {}

    for stock_code in RECOMMEND_POOL:

        time.sleep(1)
        low_pe_payload = _get_roe_payload(stock_code)
        response = _call_api(low_pe_payload)
        df = _covert_json_to_pandas_dataframe(response)

        if df.loc[0]["roe_yearly"] > 20:

            stock_roe_higer_than_20[stock_code] = df.loc[0]["roe_yearly"]

            print(f"{stock_code} YES")

    print(stock_roe_higer_than_20.keys())
