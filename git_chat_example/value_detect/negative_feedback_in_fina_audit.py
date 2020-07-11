import tushare as ts
import requests
import json
import pandas as pd
import time

TOKEN="YOUR_TOKEN"
URL="http://api.tushare.pro"

get_all_stock_codes_payload = {
    "api_name": "stock_basic",
    "token": TOKEN,
    "params": {
        "exchange": "",
        "list_status": "L",
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


def _get_audit_comment_payload(stock_code):
    return {
    "api_name": "fina_audit",
    "token": TOKEN,
    "params": {
        "ts_code": stock_code,
    }
}


if __name__ == "__main__":
    response = _call_api(get_all_stock_codes_payload)
    stock_code_list = [stock[0] for stock in response['data']['items']]

    negative_audit_feedback_stocks_list = []
    # stock_code_list = ["000011.SZ", "000012.SZ", "000013.SZ"]

    for stock_code in stock_code_list:

        time.sleep(1)
        audit_result_payload = _get_audit_comment_payload(stock_code)
        response = _call_api(audit_result_payload)
        print(response)
        if response['data']['items'][0][3]:
            audit_result = response['data']['items'][0][3]


        if audit_result != "标准无保留意见":
            negative_audit_feedback_stocks_list.append(response['data']['items'][0][0])




    print(negative_audit_feedback_stocks_list)




