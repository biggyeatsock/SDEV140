##########################################################
#  Author: Logan Luper
#  Date: 10/25/2023
#
#  A calculator for ones age based on birth years.
#
##########################################################


name = str(input("Enter your name: "))
current_age = int(input("Enter your birth year: "))

CURRENT_YEAR = 2023
AGE = CURRENT_YEAR - current_age
print(name, "was born in", current_age, "On January 1st of this year, he was", AGE, "years old.")