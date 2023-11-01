###########################################################################
#
#   Author: Logan Luper
#
#   A simple program to calculate the distance of points.
#
#   Date: November 1st, 2023
#
###########################################################################
def main():
    #Inputs from the user
    var1 = int(input("Please enter an x1 value: "))
    var2 = int(input("Please enter an x2 value: "))
    var3 = int(input("Please enter an y1 value: "))
    var4 = int(input("Please enter an y2 value: "))
    math(var1, var2, var3, var4)
    
def math(var1, var2, var3, var4):
    import math
    formula = (((var2-var1)**2) + ((var4-var3)**2)) # Maths
    print('The distance between these points is', '%.2f'%(math.sqrt(formula))) # This outputs a message stating the distance.
    
    return 'end'

main() # going to the main function ^^^


