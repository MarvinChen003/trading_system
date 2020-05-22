# 查询当前所有正常上市交易的股票列表
# list_status 上市状态： L上市 D退市 P暂停上市，默认L
# exchange 交易所 SSE上交所 SZSE深交所

import tushare as ts
import requests
import json
import pandas as pd

TOKEN="ea4fe281f13430950e3d7ad661af222ee5543e48d46198995693567d"
URL="http://api.tushare.pro"
API_NAME="stock_basic"


def _get_all_stock_code_from_ts():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "exchange": "",
            "list_status": "L",
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

    return r.json()


def _covert_json_to_pandas_dataframe():
    stocks = _get_all_stock_code_from_ts()
    fields = stocks['data']['fields']
    items = stocks['data']['items']
    stocks_dafaframe = pd.DataFrame(columns=fields, data=items)

    return stocks_dafaframe


def _pandas_datafram_to_csv(pandas_dataframe, csv_file_name):
    pandas_dataframe.to_csv(csv_file_name)


if __name__ == "__main__":
    stock_codes_dataframe = _covert_json_to_pandas_dataframe()
    _pandas_datafram_to_csv(stock_codes_dataframe, "stock_codes.csv")




