"""
arrays_program1.py

This Python program allows the user to enter a series of numbers and then calculates and displays the sum and average of those numbers. The user can enter as many numbers as they want and stop entering numbers by typing 'q'.
"""
def calculate_average(numbers: list[float]) -> float:
    # Return the average of the provided list.
    sum = 0
    i=1
    average = 0
    counter = len(numbers)
    while i != counter:
        sum = sum + float(numbers[i-1])
        i = i + 1
    average=sum/(counter-1)
    return average
    pass
    
def calculate_sum(numbers: list[float]) -> float:
    # Return the sum of the provided list.
    sum = 0
    counter = len(numbers)
    i = 1
    while i != counter:
        sum = sum + float(numbers[i-1])
        i = i + 1
    return sum  
    pass

def get_user_input() -> str:
    # Prompt the user for a number or 'q'.
    string  = input("Please enter a number, type 'q' to exit: ")
    return string
    
def print_average(average: float) -> None:
    # Print the average.
    print(f'The average is: {average}')
    pass
    
def print_sum(sum: float) -> None:
    # Print the sum.
    print(f'The sum is: {sum}')
    pass

def get_list_of_numbers() -> list[float]:
    numbers: list[float] = []

    while True:
        # TODO: Loop to get numbers from the user until quit.
        # Store numbers in array and return.
        user_input  = input("Please enter a number, type 'q' to exit: ")
        numbers.append(user_input)
        i=0        
        while numbers[i] != 'q':
            user_input = get_user_input()
            numbers.append(user_input)
            i=i+1
        break

    return numbers

def main():
    # TODO: uncomment one at a time to get working.
    numbers: list[float] = get_list_of_numbers()
    sum: float = calculate_sum(numbers)
    average: float = calculate_average(numbers)
    print_sum(sum)
    print_average(average)
    pass


if __name__ == "__main__":
    main()
