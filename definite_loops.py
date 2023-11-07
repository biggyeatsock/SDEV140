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

# def write_pyramid_row(row: int, height: int)  -> None:

#     for i in range (1, height+1):
#         for j in range(0, height-i-1):
#             print(" ",end="") # A space that will not go to the next line.
#         for j in range(0, i):
#             for number in range (1, i, 1):  #postive number climb
#                 print(number, end="")
#                 if number == i:
#                     print()
#                     break
#                 break
#             for val in range(i,0,-1): #Negative number climb.
#                 print(val,end="")
#         print()
    
#     return row, height

# def create_pyramid(height: int) -> None:
#     # Loop through write_pyramid_row to create the full pyramid
#         row = 0
#         write_pyramid_row(row,height)
#         return None

# if __name__ == "__main__":
#     height = get_input()
#     create_pyramid(height)




# rows = int(input("Enter number of rows: "))

# for i in range(rows): # This is half a pyrmid, solid left, stairs on the right.
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print('\n')

#########################################################  THIS WORKS
rows = int(input("Enter the number of rows:")) #height
counter = 1
for i in range (1, rows+1):
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

    ######################################################### THIS WORKS


    