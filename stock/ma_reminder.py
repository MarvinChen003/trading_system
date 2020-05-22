# Given a stock pool
# cal MA100/MA20
# Reminder if able to buy

import tushare as ts
import requests
import json
import pandas as pd

TOKEN="ea4fe281f13430950e3d7ad661af222ee5543e48d46198995693567d"
URL="http://api.tushare.pro"
API_NAME="daily"

MA100 = 100
MA20 = 20
LAST_TRADE_DATES = 20


def _get_daily_trades_for_specific_stocks(
        stock_codes,
        start_date,
        end_date
):
    payload = {
        "api_name": API_NAME,
        "token": TOKEN,
        "params" : {
            "ts_code": stock_codes,
            "start_date": start_date,
            "end_date": end_date,
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


def _covert_json_to_pandas_dataframe(stock_codes):
    data_last_year = _get_daily_trades_for_specific_stocks(stock_codes, "20190512", "20200514")
    fields = data_last_year['data']['fields']
    items = data_last_year['data']['items']
    records_last_year = pd.DataFrame(columns=fields, data=items)

    return records_last_year


def _pandas_datafram_to_csv(pandas_dataframe, csv_file_name):
    pandas_dataframe.to_csv(csv_file_name)


def _satisfy_ma100_ma20_strategy(stocks_dataframe):
    ts_codes = stocks_dataframe['ts_code'].unique()
    for ts_code in ts_codes:
        stock_dataframe = stocks_dataframe[stocks_dataframe['ts_code'] == ts_code]
        date_price_dict = pd.Series(stock_dataframe.close.values, index=stock_dataframe.trade_date).to_dict()
        date_desc_list = [date for date in date_price_dict.keys()]
        price_desc_list = [price for price in date_price_dict.values()]
        last_10_days_list = date_desc_list[:10]

        ma100_matrix = []
        ma20_matrix = []
        for date in last_10_days_list:
            list_index = date_desc_list.index(date)
            ma100_price_list = price_desc_list[list_index:(list_index + MA100)]
            ma20_price_list = price_desc_list[list_index:(list_index + MA20)]

            date_close_price = date_price_dict[date]
            ma100_price = sum(ma100_price_list) / 100
            ma20_price = sum(ma20_price_list) / 20

            if date_close_price > ma100_price:
                ma100_matrix.append("Upon")
            else:
                ma100_matrix.append("Under")

            if date_close_price > ma20_price:
                ma20_matrix.append("Upon")
            else:
                ma20_matrix.append("Under")

        ma100_matrix.reverse()
        ma20_matrix.reverse()

        positive_pool = []
        if all(x in ma100_matrix for x in ['Upon', 'Under']) and ma100_matrix[-1] == 'Upon':
            positive_pool.append(ts_code)

        buy_pool = []
        if ts_code in positive_pool and ma20_matrix[-1] == 'Upon':
            buy_pool.append(ts_code)

        return positive_pool, buy_pool


if __name__ == "__main__":
    stock_pool = ["603506.SH", "603530.SH", "603536.SH", "603578.SH", "603589.SH", "603535.SH"]
    str_stock_pool = ','.join(stock_pool)
    stocks_dataframe = _covert_json_to_pandas_dataframe(str_stock_pool)

    positive_stocks_pool, buy_pool = _satisfy_ma100_ma20_strategy(stocks_dataframe)
    if positive_stocks_pool:
        for stock in positive_stocks_pool:
            print(f'{stock} worth to have a trace this period of time.')

    if buy_pool:
        for stock in buy_pool:
            print(f'{stock} worth to buy this period of time.')

