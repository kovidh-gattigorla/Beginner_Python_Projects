#To make the Odd_Even_check we First we need input from user 
number = int(input('Enter the number :'))                            #Taking the input from the user

# Now making the condition for the Input number 
# As we know that even number are divisible by 2 with the reminder 0
if number%2 == 0:                                                    #We made a if condition from it as number%2==0
    print('It is Even number')
else :                                                               #Else It is odd
    print('It is Odd number')