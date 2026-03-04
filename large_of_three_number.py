# To make the learge_of_three_numbers we need 3 inputs from the user
num1 = float(input('Enter the 1 number :'))                             #For the first input
num2 = float(input('Enter the 2 number :'))                             #For the second input
num3 = float(input('Enter the 3 number :'))                             #For the third input
# Now comparing the three inputs by conditions
if num1>=num2 and num1>=num3:
    print('1 number is grater')
elif num2>=num1 and num2>=num3:
    print('2 number is grater')
else :
    print('3 number is grater')