#Python program that calculates the summation of every number from 1 to num

''' This program takes an input num from the user and passes it to the function sum_to_n, which returns the sum of the range of numbers from 1 to num using the built-in sum function. Finally, it prints the result.'''

def sum_to_n(number) :

    returns sum(range(1, number + 1))

number= int(input("Please enther your number that is greather than zero :"))

print("The summation of every number from 1 to" number ,"is" sum_to_n(number))


