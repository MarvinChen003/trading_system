from pe_lower_than_25 import STOCK_PE_DICT
from audit_negative_stocks import AUDIT_NEGATIVE_LIST
from debt_asset_lower_than_50 import LOW_DEBT_TO_ASSET


def _pe_lower_than_12(stock_pe_dict):
    pe_lower_than_12 = {}
    for stock, pe in STOCK_PE_DICT.items():
        if pe < 12:
            pe_lower_than_12[stock] = pe

    return pe_lower_than_12


if __name__ == "__main__":
    stock_pe_lower_than_12 = _pe_lower_than_12(STOCK_PE_DICT)

    # pe lower than 12 and audit result is not negative
    for stock in list(stock_pe_lower_than_12.keys()):
        if stock in AUDIT_NEGATIVE_LIST:
            del stock_pe_lower_than_12[stock]

    # pe < 12 and audit good and debet to asset < 50%
    for stock in list(stock_pe_lower_than_12.keys()):
        if stock not in LOW_DEBT_TO_ASSET:
            del stock_pe_lower_than_12[stock]

    print(stock_pe_lower_than_12.keys())