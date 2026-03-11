# To make the age calculator first we need to impoer datetime module For the present date
from datetime import date                                             # We need only date from the date time module

# Now we need three inputs for year month date
year = int(input('Enter the year of birth : '))                       # For the users Year
month = int(input('Enter the month of birth : '))                     # For the users Month
day = int(input('Enter the day of birth : '))                         # For the users Day

# For the date of birth in its (YYY,MM,DD)
birth_date = date(year,month,day)                                     # Taking a viarable to store it in the from

# For Todays date
today = date.today()                                                  # .today() is from the module 

# Making the age
age = today.year - birth_date.year                                   # Today - DOB is the age so

# If condition for the other 

# Now printing it
print(age)
