# Here the Temperature will be converted form C->F or F->C
# So the formul for the converting is F = (C*9/5)+32 or F = (c*1.8)+32 We will be using the first one as based on the C formula
# The second formuls for it is converting from C = (F-32)*5/9 
# Lets make Two Def Functions
def celsius_to_fahrenheit(c):                                # Function for converting from celsius to fahrenheit
    return (c*9/5)+32
def fahrenheit_to_celsius(f):                                # Function for converting from fahrenheit to celsius
    return (f-32)*5/9

# Giving the options for the user
print('Temperature Converter')                               # Text for output For user
print('1. Celsius to Fahrenheit')                            # Text for output For user
print('2. Fahrenheit ro Celsius')                            # Text for output For user

choic = input('select 1 or 2 :')                             # For the users Choice 

if choic == '1':                                             # If condition if 1 is input by user
    c = float(input('Enter the Temperature in Celsius :'))   # Input of the celsius to find the fahrenheit
    f = celsius_to_fahrenheit(c)                             # For the fahrenheit Formuls simplifacation by the the given input of c
    print(f'{c} Celsius = {f:.2f} Fahrenheit')               # Printing the out put {c} before celsius  and {f} after :.2f is used the Given the extra 2 decimals like 0.00
elif choic == '2':                                           # Elif for the another choice
    f = float(input('Enter the Temperature in Fahrenheit :'))# For the input of fahrenheit
    c = fahrenheit_to_celsius(f)                             # For the fahrenheit to find the celsius
    print(f'{f} Fahrenheir = {c:.2f} Celsius')               # Print for he out put
else :                                                       # If non of then then this will be taken
    print('Not a Selection . (1 or 2)')                      # Print the out put of incorrect selection