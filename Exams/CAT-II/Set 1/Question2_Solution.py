# ---------(a)---------
# Algorithm:
'''
-> First, we will ask the user to input N (number of distinct objects)
-> Next, we will initialize factorial = 1
-> Next, we will enter a for loop and multiply the value of i to factorial in every iteration of the loop
-> Now, we will print the output as "{N}! = {factorial}"
'''
# Program Start:
N = int(input("Enter number of distinct objects: "))

factorial = 1
for i in range(1,N+1):
    factorial = factorial*i

print(f"{N}! = {factorial}")

# ---------(b)---------
# Algorithm:
'''
-> To deal with the user enterring negative integers, we will force the user to enter a positive integer using a while loop in the input sequence
-> Then, we will add a simple if-else check to see if N = 0 or not, if N = 0 then we will hardcode the response 0! = 1
'''
# Program Start:
N = int(input("Enter number of distinct objects: "))
while N < 0:
    print("Please enter a positive integer")
    N = int(input("Enter number of distinct objects: "))

if N == 0:
    print("0! = 1")
else:
    factorial = 1
    for i in range(1,N+1):
        factorial = factorial*i

    print(f"{N}! = {factorial}")

# Test cases: 
'''
If N = -1:
-> Please enter a positive integer
-> Enter number of distinct objects: 
this will happen indefinitely until the user enters a positive integer

If N = 0:
-> 0! = 1

If N = 5:
-> 5! = 120
'''
