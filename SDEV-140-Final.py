###################################
#
#   Author: Logan Luper
#   December 12th, 2023
#   This program will parse a file and gather data from it to display 
#   the number of doctor visits.
#
###################################"
FILE_PATH = 'SDEV140\data.dat'
from datetime import datetime

def GetUserInput():

    usinput = input("Enter an account number, or 'q' to quit:")
    if usinput == 'q':
        exit()
    return usinput

def parsed_file(FILE_PATH):
    parsed_vals = []
    with open(FILE_PATH, 'r') as file:  # Open the file in read mode        
        for line in file:
            # remove '~' character between the data
            items = line.replace('~', ',')
            items = items.strip()
            parsed_vals.append(items)
        return parsed_vals

def cleaned_data(data):
    FormattedData = []
    AccountID = ' '
    DateVisited = ' '
    LineNumber = 1
    for DataRow in data:
        # Acount ID
        AccountID = DataRow[0]
        if len(AccountID) == 0:
            raise ValueError(f'Error on line {LineNumber}: ID must be 5 characters long.')
            
        # Date Visited
        DateVisited = DataRow[1]
        if DateVisited != '':
            try:
                datetime.strptime(DateVisited, '%Y-%m-%d')
            except ValueError:
                raise ValueError(f'Error on line {LineNumber}: Date is empty')



        FormattedData.append([AccountID, DateVisited])
        LineNumber += 1
    return FormattedData

def main():
    usinput = GetUserInput()
    try: # parsing data
        data = parsed_file(FILE_PATH)
    except FileNotFoundError as e:
        print(f'File not found ' + e)
        exit()
    print(data, '\n This is all data: \n')
    if len(data) == 0: # if file is empty this will exit.
        print('File is empty.')
        exit()
    
    # FormattedData = cleaned_data(data)
    
    # print('This is the formatted data.',FormattedData)


main()