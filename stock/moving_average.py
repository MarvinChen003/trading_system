import tushare as ts
import requests
import json
import pandas as pd

TOKEN="PLEASE_USE_YOUR_OWN_TOKEN_TO_TUSHARE"
URL="http://api.tushare.pro"
API_NAME="daily"

MA100 = 100
MA20 = 20


def _get_one_year_data_for_specific_stock():
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "ts_code": "603506.SH",
            "start_date": "20190512",
            "end_date": "20200514",
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


def _covert_json_to_pandas_obj():
    data_last_year = _get_one_year_data_for_specific_stock()
    fields = data_last_year['data']['fields']
    items = data_last_year['data']['items']
    records_last_year = pd.DataFrame(columns=fields, data=items)

    return records_last_year


def _ma100_ma20():
    data_last_year = _covert_json_to_pandas_obj()
    data_last_100_days = data_last_year[:MA100]
    data_last_20_days = data_last_year[:MA20]
    avg_price_ma100 = data_last_100_days['close'].mean()
    avg_price_ma20 = data_last_20_days['close'].mean()
    price_last_day = data_last_100_days['close'].values[0]

    # df = pd.DataFrame(data_last_year)
    print(avg_price_ma100)
    print(avg_price_ma20)
    print(price_last_day)


if __name__ == "__main__":
    _ma100_ma20()
