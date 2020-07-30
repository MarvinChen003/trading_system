import tushare as ts
import requests
import json
import pandas as pd
import time


TOKEN = "YOUR_TOKEN"
URL = "http://api.tushare.pro"

get_all_stock_codes_payload = {
    "api_name": "stock_basic",
    "token": TOKEN,
    "params": {"exchange": "", "list_status": "L",},
}


def _call_api(payload):

    payload

    headers = {
        "Accept": "application/json",
    }

    r = requests.post(URL, data=json.dumps(payload), headers=headers,)

    return r.json()


def _get_pe_payload(stock_code):
    return {
        "api_name": "daily_basic",
        "token": TOKEN,
        "params": {"ts_code": stock_code, "trade_date": "20200710"},
    }


if __name__ == "__main__":
    response = _call_api(get_all_stock_codes_payload)
    stock_code_list = [stock[0] for stock in response["data"]["items"]]

    good_pe_stocks_dict = {}
    # stock_code_list = ["000011.SZ", "000012.SZ", "000013.SZ"]
    stock_checked_list = []
    filename = "stock_checked.txt"
    with open(filename, "w") as file_object:
        try:
            for stock_code in stock_code_list:
                stock_checked_list.append(stock_code)
                file_object.write(f"{stock_code} ")
                time.sleep(1)
                pe_payload = _get_pe_payload(stock_code)
                response = _call_api(pe_payload)
                if response["data"]["items"]:
                    stock_item = dict(enumerate(response["data"]["items"][0]))
                    if stock_item.get(6) is not None and stock_item.get(6) < 25:
                        good_pe_stocks_dict[stock_item[0]] = stock_item[6]
                        print(stock_item[0], stock_item[6])
        finally:
            print(stock_checked_list)

    print(good_pe_stocks_dict)
