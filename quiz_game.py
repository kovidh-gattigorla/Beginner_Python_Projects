# For the welcome to print for the Player
print('Welcome to the QUIZ :) \n')
# For the input to the Player 
PLAY = input('Do you want to play the game ? :')
# if Yes it will take to the game i used != for not equla to and .lower() for the any kind of answer Yes or YES of yes because python is a k sensitive language
if PLAY.lower() != 'yes':
    exit()                                  # To exit from the if condition
# This lanes are still under the if condition
a = input('What is Your name : ')
print('Lets Go',a)
# Here i am taking the a as the variable to store the input of the user, for the Question 
a = input('What is 2+3 : ')
if a == '5':                                # If input is 5 so ('here i got a problem that is 5 can be taken as string so i used '5')
    print ('correcct :)')                 # If it is correct it will print correct
else :                                      # Else it will print the below command
    print('Incorrect ?')
# Here i take again a(as the work of 'a' variable will end for the else condition used before) if not i can also take the variable
a = int(input('What is 5+2 : '))            # i used int for the input to be integer as the answer will be takin as the integer
if a == 7 :                                 # If the a == 7 here 7 will be taken as int
    print('Correct :)')                   # It will print Correct
else :                                      # If not Incorrect bellow print statment will printed
    print('Incorrect ?')
# Again using a variable for the next question 


