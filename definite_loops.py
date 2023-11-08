############################
#
#  Author: Logan Luper
#  Date: November 6th, 2023.  
#  A simple pyramid program.
#
#############################

# def get_input() -> int:
#     ## Prompt the user for input and return it as the correct data type.
#     height = int(input("Enter the number of rows:")) #height
#     return height

# def write_pyramid_row(row: int, lcount:int)  -> None:
#     for j in range(0, rows-lcount):
#         print(" ",end="") # A space that will not go to the next line.
#         for j in range(0, lcount):
#             if counter != lcount+1:
#                 for number in range (1, lcount, 1):  #postive number climb
#                     print(number, end="")
#                 for val in range(lcount,0,-1): #Negative number climb.
#                     print(val, end="")
#             counter=counter+1

#     print()
#     return None

# def create_pyramid(rows: int) -> None:
#     # Loop through write_pyramid_row to create the full pyramid
#     counter = 1
#     lcount = 0
#     for i in range (1, rows+1):
#         write_pyramid_row(rows, lcount)
#         lcount=lcount+1 
#     return None
    

# if __name__ == "__main__":
#     rows = get_input()
#     create_pyramid(rows)

# print('End')

#########################################################  THIS WORKS
rows = int(input("Enter the number of rows:")) #height
counter = 1
for i in range (1, rows+1): # How many rows get built.
    for j in range(0, rows-i):
        print(" ",end="") # A space that will not go to the next line.
    for j in range(0, i):
        if counter != i+1:
            for number in range (1, i, 1):  #postive number climb
                print(number, end="")
            for val in range(i,0,-1): #Negative number climb.
                print(val, end="")
            counter=counter+1
         
    print()
print('\nEnd')
    ######################################################### THIS WORKS


    