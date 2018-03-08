from stock_quote import *


def parse_stock_quote(stock_code):
    stock_dump = get_stock_quote(stock_code)
    stock_dict = dict()
    stock_dict['open_price'] = stock_dump['open']
    stock_dict['close_price'] = stock_dump['closePrice']
    stock_dict['company_name'] = stock_dump['companyName']
    return stock_dict


def read_input():
    stock_code = input('Enter NSE stock code : ')
    stock_day_val = parse_stock_quote(stock_code)
    print(stock_day_val)


if __name__ == "__main__":
    read_input()
