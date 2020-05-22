import pandas as pd


def _fetch_main_board_stocks():
    all_stocks_df = pd.read_csv("stock_codes.csv")
    main_board_stocks_df = all_stocks_df[all_stocks_df['market'] == "主板"]

    return main_board_stocks_df


def _fetch_available_trade_dates():
    all_dates_df = pd.read_csv("trade_dates.csv")
    available_trade_dates = all_dates_df[all_dates_df['is_open'] == 1]

    return available_trade_dates


def _fetch_out_daily_trade(stock_dataframe, trade_dates):
    stock_code_name_dict = pd.Series(stock_dataframe.name.values, index=stock_dataframe.ts_code).to_dict()
    trade_dates_list = trade_dates['cal_date'].tolist()
    trade_dates_list.reverse()
    print(trade_dates_list)
    # TODO get_today, cal ma 100, compare with today's close price, if close > ma100 keep, otherwise drop



if __name__ == "__main__":
    main_board_stocks_df = _fetch_main_board_stocks()
    trade_dates = _fetch_available_trade_dates()
    _fetch_out_daily_trade(main_board_stocks_df, trade_dates)

