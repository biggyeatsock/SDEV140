from datetime import datetime

# pass in the file name, open and read through the file.
# return a list of lists representing rows in the file.
def read_file_into_list(file_name):
    parsed_vals = [] # Initialize an empty list to store the parsed values
    
    with open(STUDENTS_FILE_PATH, 'r') as input_file:
        rows = input_file.readlines() # Read all the lines from the file
        for row in rows:
            items = row.split(',') # Split the row into a list of values'

            for i in range(0, len(items)):
                items[i] = items[i].strip() # Remove any leading or trailing whitespace from the items)
    
            parsed_vals.append(items) # Add the parsed values to the list
    return parsed_vals

def check_header_row(header_row, expected_fields):
    if len(header_row) != len(expected_fields):
        print('Header row has the wrong number of fields.')
        return False
    
    for i in range(0, len(expected_fields), 1):
        if header_row[i].lower() != expected_fields[i]:
            return False
    
    return True

def clean_validate_data_rows(data_rows, first_data_line_number):
    cleaned_data = []
    
    line_number = first_data_line_number
    for data_row in data_rows:
        studentid = ''
        first_name = ''
        last_name = ''
        dob = ''
        grade = ''
        
        # STUDENT ID
        studentid = data_row[0]
        if len(studentid) != 6:
            raise ValueError(f'Error on line {line_number}: ID must be 6 characters long.')
        # NAME
        name_parts = data_row[1].split(' ')
        if len(name_parts) != 2:
            raise ValueError(f'Error on line {line_number}: Name must be in the format "First Last".')
        first_name = name_parts[0]
        last_name = name_parts[1]
        # STUDENT DOB
        dob = data_row[2]
        if dob != '':
            try:
                date = datetime.strptime(dob, '%Y-%m-%d')
            except ValueError:
                raise ValueError (f'Error on line {line_number}: DOB must be in the format "YYYY-MM-DD".')
        # STUDENT GRADE
        VALID_GRADES = ['A', 'B', 'C', 'D', 'F']
        grade = data_row[3]
        if grade.upper() not in VALID_GRADES:
            raise ValueError(f'Error on line {line_number}: Grade must be one of the following: {", ".join(VALID_GRADES)}.')


        cleaned_data.append([studentid, first_name, last_name, dob, grade])
        line_number += 1 
    return cleaned_data


def display_output(cleaned_data, header_fields):
    # printing header row
    print('Student ID, Last Name, First name, Date of Birth, Grade')
    print('-------------------------------------------------------')
    for data_row in cleaned_data:
        print('{:<10}{:<10}{:<10}{:<10}{:<6}'.format(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4]))
        
    


def remove_duplicates(cleaned_data):
    deduped_data = []
    added_items = []
    
    for data_row in cleaned_data:
        if data_row[0] not in added_items:
            deduped_data.append(data_row)
            added_items.append(data_row[0])

    return deduped_data

if __name__ == '__main__':
    STUDENTS_FILE_PATH = 'SDEV140\students.csv'
    HEADER_FIELDS = ['id', 'name', 'dob', 'grade']
    
    try: 
        parsed_data = read_file_into_list(STUDENTS_FILE_PATH)
    except FileNotFoundError as e:
        print(f'File not found: ' + str(e))
        exit()
    
    # Checking for an empty file.
    if len(parsed_data) == 0:
        print('File is empty.')
        exit()
    
    header_row = parsed_data[0] # Get the header row
    if not (check_header_row(header_row, HEADER_FIELDS)):
        print('Header row is incorrect, not in expected format.', HEADER_FIELDS)
        exit()

    data_rows = parsed_data[1:] # Get the data rows
    first_data_line_number = 2 # The first data line number is 2, since the header row is 1
    try: 
        cleaned_data = clean_validate_data_rows(data_rows, 2)
    except ValueError as e:
        print(e)
        exit()
    cleaned_data = remove_duplicates(cleaned_data)

    display_output(cleaned_data, HEADER_FIELDS)
