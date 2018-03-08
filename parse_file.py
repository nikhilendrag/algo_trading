import csv


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    nested_dict = dict()
    
    with open(filename, 'rt') as csvfile:
        csv_data = csv.DictReader(csvfile, delimiter=separator, quotechar = quote)
        
        for entry in csv_data:
            row_id = entry[keyfield]
            nested_dict[row_id] = entry
    
    return nested_dict
    
    
def parse_holdings_file(file_name):
    holdings_dict = read_csv_as_nested_dict(file_name, 'Instrument', ',', '"')
    return holdings_dict


def read_input():
    file_name = input('Enter holdings file name : ')
    
    if file_name=='':
        file_name = 'holdings.csv'
        
    holdings_dict = parse_holdings_file(file_name)
    print(holdings_dict)


if __name__ == "__main__":
    read_input()
