# To make the factorial calculator we need input from user
num = int(input('Enter the Number: '))                                   # Input from user
# Taking some value fo factorial
factorial = 1                                                            
# Using for loop making the count of every element
for i in range (1,num+1):                                                # For i in range from 1 to the input number from user
    factorial = factorial*i                                              # Saving the factorial as 1*i(here i is in loop so it will be counting every element)
print('Factorial of', num , 'is', factorial)