import pandas as pd

python_data = {'request_id': '1ff7b67a9b5d11ea9d1865bfe1830d051590063485881330', 'code': 0, 'msg': '', 'data': {'fields': ['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close', 'change', 'pct_chg', 'vol', 'amount'], 'items': [['603506.SH', '20200513', 21.73, 22.49, 21.24, 22.48, 21.56, 0.92, 4.2672,22575.41, 49810.984], ['603506.SH', '20190515', 23.5, 23.9, 23.48, 23.69, 23.43, 0.26, 1.1097, 6751.2, 16025.358], ['603506.SH', '20190514', 23.38, 23.54, 23.03, 23.43, 23.41, 0.02, 0.0854, 5755.3, 13441.287], ['603506.SH', '20190513', 23.09, 23.55, 22.91, 23.41, 23.32, 0.09, 0.3859, 4973.6, 11542.756]], 'has_more': False}}

fields = python_data['data']['fields']
items = python_data['data']['items']
pandas_df = pd.DataFrame(columns=fields, data=items)

print(pandas_df['close'])