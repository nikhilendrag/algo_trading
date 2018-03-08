from parse_holdings import parse_holdings_csv
from email_client import email_report
from email_client import formatted_date
from write_to_file import write_file


def email_daily_report(report_file_name):
    holdings_daily_vals = parse_holdings_csv(report_file_name)
    outfile = "holdings_statement_" + formatted_date() + '.txt'
    write_file(holdings_daily_vals, outfile)
    email_report(outfile)


if __name__ == "__main__":
    file_name = input('Enter the holdings file name :')
    if file_name == '':
        file_name = 'holdings.csv'
    email_daily_report(file_name)
