# Logan Luper, October 30th, 2023.
#
# This program will sort the three inputs and output the numbers in smallest to largest format.

first_input = int(input('Please enter an input: '))
second_input = int(input('Please enter a second input: '))
third_input = int(input('Please enter a third input: '))

if first_input > second_input:
    if first_input > third_input:
        if second_input > third_input:
            print('The ordered list of integers is:',third_input,',', second_input,',', first_input)# 3, 2, 1, in order.
        else:
            print('The ordered list of integers is:',second_input,',', third_input,',', first_input)# 2, 3, 1
    elif third_input > first_input:
        if third_input > second_input:
            if first_input > second_input:
                print('The ordered list of integers is:',second_input,',', first_input,',', third_input) # 3rd, 1st, 2nd
            else:
                print('The ordered list of integers is:',third_input,',', second_input,',', first_input) # 3rd, 2nd, 1st

elif second_input > first_input:
    if second_input > third_input:
        if first_input > third_input:
            print('The ordered list of integers is:',third_input,',', first_input,',', second_input) # 2nd, 1st, 3rd.
        else:
            print('The ordered list of integers is:',first_input,',', third_input,',', second_input) #2nd, 3rd, 1st
    elif third_input > first_input:
        if third_input > second_input:
            if first_input > second_input:
                print('The ordered list of integers is:',second_input,',', first_input,',', third_input) # 3rd, 1st, 2nd
            else:
                print('The ordered list of integers is:',first_input,',', second_input,',', third_input) # 3rd, 2nd, 1st
