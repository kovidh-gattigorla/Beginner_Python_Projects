# To make the simple_intrest_calculater We need principal,rate,time .
# So we take 3 inputs by the user
principal = float(input('Enter the Principal :'))                                      #Inputing the principal by user
rate = float(input('Enter the rate in % :'))                                           #Inputing the rate by user
time = float(input('Enter the time in years :'))                                       #Imputing the time by user
# As for the formula of intrest we need to multiply them all and divid them by 100
simple_intrest = principal*rate*time/100                                               #We are storing the multiplication and dividing in another variable
# Now we need to print them 
print('Simple intrest is :',simple_intrest)                                            #For the simple intrest
print('Total Amount will be :',principal+simple_intrest)                               #For the total amount by principal+simple intrest