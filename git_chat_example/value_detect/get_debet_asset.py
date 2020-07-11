from pe_lower_than_25 import STOCK_PE_DICT

import tushare as ts
import requests
import json
import pandas as pd
import time


TOKEN="YOUR_TOKEN"
URL="http://api.tushare.pro"


def _get_low_pe_stock_payload(stock_code):
    return {
    "api_name": "fina_indicator",
    "token": TOKEN,
    "params": {
        "ts_code": stock_code,
    }
}


def _call_api(payload):

    payload

    headers = {
        "Accept": "application/json",
    }

    r = requests.post(
        URL,
        data=json.dumps(payload),
        headers=headers,
    )

    return r.json()


def _covert_json_to_pandas_dataframe(json_data):
    fields = json_data['data']['fields']
    items = json_data['data']['items']
    dafaframe = pd.DataFrame(columns=fields, data=items)
    return dafaframe


if __name__ == "__main__":

    stock_low_debt_to_asset = {}

    for stock_code in STOCK_PE_DICT.keys():

        time.sleep(1)
        low_pe_payload = _get_low_pe_stock_payload(stock_code)
        response = _call_api(low_pe_payload)
        df = _covert_json_to_pandas_dataframe(response)
        print(stock_code, df.loc[0]['debt_to_assets'])
        if int(df.loc[0]['debt_to_assets']) < 50:

            stock_low_debt_to_asset[stock_code] = df.loc[0]['debt_to_assets']

            print(f'{stock_code} YES')

    print(stock_low_debt_to_asset)

