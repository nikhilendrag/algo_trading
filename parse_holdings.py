from parse_file import *
from parse_stock_quote import *


def parse_holdings_csv(file_name):
    nested_dict = parse_holdings_file(file_name)

    daily_stats_dict = dict()
    for stock in nested_dict:
        stock_daily_val = parse_stock_quote(nested_dict[stock]['Instrument'])
        daily_stats_dict[stock_daily_val['company_name']] = stock_daily_val
    return daily_stats_dict


def display_daily_stock_stats(daily_stats):
    print("Company                                               Open     Close")
    for stock in daily_stats:
        print('{:50}'.format(stock), '{:>8.2f}'.format(daily_stats[stock]['open_price']),
              '{:>8.2f}'.format(daily_stats[stock]['close_price']))


def read_input():
    file_name = input('Enter holdings file name : ')

    if file_name == '':
        file_name = 'holdings.csv'

    daily_stats = parse_holdings_csv(file_name)
    display_daily_stock_stats(daily_stats)


if __name__ == "__main__":
    read_input()
