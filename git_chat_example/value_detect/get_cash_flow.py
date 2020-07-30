import tushare as ts
import requests
import json
import pandas as pd


TOKEN = "YOUR_TOKEN"
URL = "http://api.tushare.pro"
API_NAME = "cashflow"


def call_api():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params": {"ts_code": "603506.SH",},
    }

    headers = {
        "Accept": "application/json",
    }

    r = requests.post(URL, data=json.dumps(payload), headers=headers,)

    # print(r.json())
    stock_cash_flow = _covert_json_to_pandas_dataframe(r.json())
    net_profit_2020 = stock_cash_flow[stock_cash_flow["ann_date"] == "20190430"]
    print(net_profit_2020.iloc[1]["net_profit"])


def _covert_json_to_pandas_dataframe(json_data):
    fields = json_data["data"]["fields"]
    items = json_data["data"]["items"]
    dafaframe = pd.DataFrame(columns=fields, data=items)

    # print(dafaframe)
    return dafaframe


if __name__ == "__main__":
    call_api()
