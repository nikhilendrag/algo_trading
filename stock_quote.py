from nsetools import Nse


def get_stock_quote(stock_code):
    nse = Nse()
    stock_dict = nse.get_quote(stock_code)
    return stock_dict


def read_input():
    stock_code = input('Enter NSE stock code : ')
    stock_dict = get_stock_quote(stock_code)
    print(stock_dict)


if __name__ == "__main__":
    read_input()
