import tushare as ts
import requests
import json
import pandas as pd


TOKEN="PLEASE_USE_YOUR_OWN_TOKEN_TO_TUSHARE"
URL="http://api.tushare.pro"
API_NAME="trade_cal"


def _get_trade_dates():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "exchange": "",
            "start_date": "20190515",
            "end_date": "20200516",
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
    trade_dates = _get_trade_dates()
    fields = trade_dates['data']['fields']
    items = trade_dates['data']['items']
    trade_dates_df = pd.DataFrame(columns=fields, data=items)

    return trade_dates_df


def _pandas_dataframe_to_csv(pandas_dataframe, csv_file_name):
    pandas_dataframe.to_csv(csv_file_name)


if __name__ == "__main__":
    trade_dates_df = _covert_json_to_pandas_dataframe()
    _pandas_dataframe_to_csv(trade_dates_df, "trade_dates.csv")




