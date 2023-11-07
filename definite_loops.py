############################
#
#  Author: Logan Luper
#  Date: November 6th, 2023.  
#  A simple pyramid program.
#
#############################


# # def get_input() -> int:
# #     ## Prompt the user for input and return it as the correct data type.
# #     height = int(input("Enter the pyramid height: "))
# #     return height

# # def write_pyramid_row(row: int, height: int)  -> None:
# #     # Print spaces before numbers
# #     for row in range(height-1,0,-1):
# #         print(' ')
# #     # Print increasing numbers
# #     for i in range(0,height-row,1):
# #         print(i, end=" ")

# #     # Print decreasing numbers (if there are any)
    
# #     return row, height

# # def create_pyramid(height: int) -> None:
# #     # Loop through write_pyramid_row to create the full pyramid
# #     for i in range(0,height,1):
# #             write_pyramid_row(i,height)
# #     return None

# # if __name__ == "__main__":
# #     height = get_input()
# #     create_pyramid(height)




# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print('\n')

rows = int(input("Enter the number of rows:"))
counter = 1
for i in range (0, rows):
    for j in range(0, rows-i-1):
        print(" ",end="") # A space that will not go to the next line.
    for j in range(0, i):
        if counter != i:
            for number in range (1, i, 1):
                print(number, end="")
            for val in range(i,1,-1):
                print(val, end="")
            counter=counter+1
         
    print()


    