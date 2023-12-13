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
    usinput = input("\nEnter an account number, or 'q' to quit: ")
    if usinput == 'q':
        exit()
    return usinput


def parsed_file(FILE_PATH): # All good!
    data = {}
    invalid_dates_data = {}
    with open(FILE_PATH, 'r') as file:
        for line in file:
            elements = line.strip().split('~')
            account_number = elements[0]
            dates = elements[1:]
            if len(account_number) != 5:
                print(f"\nAccount Number {account_number} is not 5 characters long. \nSkipping.")
                continue

            validated_dates = []
            invalid_dates = []
            for date_str in dates:
                if date_str.strip():  # Check if date_str is not empty
                    try:
                        date_obj = datetime.strptime(date_str.strip(), '%Y/%m/%d')
                        validated_dates.append(date_obj.strftime('%Y/%m/%d'))
                    except ValueError:
                        invalid_date = date_str.strip()
                        if account_number in invalid_dates_data:
                            invalid_dates_data[account_number].append(invalid_date)
                        else:
                            invalid_dates_data[account_number] = [invalid_date]
                        print(f"Invalid date '{invalid_date}' for Account Number {account_number}. \nSkipping.")
            

            if validated_dates:
                if account_number in data:
                    data[account_number].extend(validated_dates)
                else:
                    data[account_number] = validated_dates

    return data, invalid_dates_data


def search(data, invalid_dates_data, usinput): # All good!
    if usinput in data:
        print(f'Account ID: {usinput}', end=' ')
        dates = data[usinput]
        if dates:
            print(f"{dates[0].replace('/', '')};{dates[-1].replace('/', '')}")
        else:
            print()
    elif usinput in invalid_dates_data:
        print(f"Account ID: {usinput}")
        invalid_dates = invalid_dates_data[usinput]
        if invalid_dates:
            for date in invalid_dates:
                print(f"Invalid date: {date}")
    else:
        print(f"Account Number {usinput} not found.")


def main():
    try:
        data, invalid_dates_data = parsed_file(FILE_PATH)
    except FileNotFoundError as e:
        print(f'File not found ' + e)
        exit()

    if len(data) == 0:
        print('File is empty.')
        exit()

    usinput = GetUserInput()
    while usinput != 'q':
        search(data, invalid_dates_data, usinput)
        usinput = GetUserInput()

main()