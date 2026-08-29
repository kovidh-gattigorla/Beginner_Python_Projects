# To make the fibonacci series we need the input form user
num = int(input('Enter the Number'))
# Using the def 
def fibonacci(n):                                               # Using the def to call the functin                         
    if n<=1:                                                    # If n is <or = to 1 
        return n                                                # It will be returning the n
    else :                                                      # else condition
        return fibonacci(n-1)+fibonacci(n-2)                    # it will be returning n-1+n-2 meains if n=3 then 1+2 
# Using the for loop for the i to prit every element of the range
for i in range(num):                                            # For i in range of input number eg:3
    print(fibonacci(i))                                         # Printing the every loop elements