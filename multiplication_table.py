# To make the multiplication table we need yours input
num = int(input('Enter the Number :'))                             # For users input

# Now we need loop because we need it from 1 to 10 so 
for i in range (1,11):                                             # Need it for the next numbers to print
    print(num,'x',i,'=', num*i)