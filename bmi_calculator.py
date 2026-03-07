# To make the bmi_calculator we need to inputs from the user
weight = float(input('Enter your Weight in kilograms :'))                            # For the weight input
height = float(input('Enter your Height in meters :'))                                 # For the hight input
# As we completed the two inputs
# Now we need to implement the formula bmi=weight/hight^2
bmi = weight/(height**2)                                                            # Here we need to use (for the hightand**2) because the power is bilong to hight only
# Printing the round of the bmi
print('your bmi is :', round(bmi,2))                                                # Here we give rount of bmi,2 indicated two integers
# Now the Catagary
if bmi < 18.5 :
    print('You are Underweight')                                                    # If the bmi is less then 18.5
elif bmi <24.9 :
    print('You are Normal')                                                         # If the bmi is less then 24.5
elif bmi <29.9 :
    print('You are OverWeight')                                                     # If the bmi is less then 29.9
else :
    print('You are Obese')                                                          # else this one