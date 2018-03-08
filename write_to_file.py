

def write_file(holdings_daily_vals, outfile):
    fd = open(outfile, 'wt')
    fd.write("Company                                             Open     Close\n")
    for stock in holdings_daily_vals:
        fd.write('{:50}'.format(stock) + '{:>8.2f}'.format(holdings_daily_vals[stock]['open_price']) +
                 '{:>8.2f}'.format(holdings_daily_vals[stock]['close_price']) + '\n')
