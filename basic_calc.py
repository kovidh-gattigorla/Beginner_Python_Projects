# To make a Calculater we need Two inputs in integer.
Number_1 = int(input('Enter First Number: '))                           #Given the first input in Number_1
Number_2 = int(input('Enter Second Number: '))                          #Given the second input in Number_2

# After taking the inputs We need Arithmetic operations.
# We can take Them directly or Indiractly.
# I took in direct .But it is giving some Division Error like zerodivisinError .So i keep it in the conditin state.
add = Number_1 + Number_2                                               #Adding two inputs in Add
sub = Number_1 - Number_2                                               #Subtracting two inputs in Sub
mul = Number_1 * Number_2                                               #Multiplication Two inputs in Mul

# We Need to give Some option for the operation                                              
print('Select One opiton')                                              #Just Normal Text For INFO
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Dividion')

# Taking the option Through Input For the exact operation from User 
selection = input('Enter the selection (1/2/3/4):')                     #Taking the option to make the Arithmetic Operation

# Using the conditon for Different outputs By the selected option
if selection == '1' :                                                   #If condition for 1 Option
    print('Addition is :',add)
    
elif selection == '2':                                                  #elif Condition for 2 Option
    print('Subtraction is :',sub)
 
elif selection == '3':                                                  #elif Condition for 3 Option
    print('Multiplication is :',mul)

elif selection == '4' :                                                 #elif Condition for 4 option
    if Number_2 != 0:                                                   # Sub Condition for 4 option if not 0
        div = Number_1 / Number_2                                       #I put the Div because of 'ZeroDivisionError'
        print('Dividion is :',div)                       
    else:                                                               # Sub Condition for 4 option else 
        print('Error')     
else:                                                                   #If non of the Above is true
    print('Not from Above option')
