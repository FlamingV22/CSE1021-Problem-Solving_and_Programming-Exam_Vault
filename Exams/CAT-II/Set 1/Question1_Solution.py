# ---------(a)---------

# Algorithm: 
'''
-> We will first make a list with the value of the first two terms as 2 and 3 according to the problem statement. 
-> Next, we will ask the user to input the value of integer N
-> Next, we will check if the user has enterred N = 1 or N = 2, If they have, then we will give the output as "2" or "2 3"
-> Next, we will enter a for loop to generate a total of N term and print them
'''
# Start Program
terms = [2,3]

N = int(input("Enter number of terms: "))

if N == 1: 
    print(terms[0])
else: 
    print(terms[0], terms[1], end = " ")
    for i in range(2,N):
        next_term = terms[i-2] + terms [i-1]
        terms.append(next_term)
        print(next_term, end = " ")

# ---------(b)---------

# Algorithm:
'''
-> We will initialize a counter named 'total' to 0
-> Next, we will add another line inside our for loop to increment total by next_term
-> Next, we will add a final print statement outside the for loop to show our total counter at the end
'''
# Start Program
terms = [2,3]

N = int(input("Enter number of terms: "))

total = 0
if N == 1: 
    print(f"{terms[0]} \n Total: {total + terms[0]}") 
else: 
    print(terms[0], terms[1], end = " ")
    for i in range(2,N):
        next_term = terms[i-2] + terms [i-1]
        terms.append(next_term)
        Total += next_term
        print(next_term, end = " ")
if N == 2:
    print(f"\nTotal: {total + terms[0] + terms[1]}")
else:
    print(f"\nTotal: {total}")

# ---------(c)---------
# N = 1: 
'''
Output will be: 
-> 2
-> Total: 2
'''
# N = 2:
'''
Output will be:
-> 2 3
-> Total: 5
'''
# N = 7
'''
Output will be:
-> 2 3 5 8 13 21 34
-> Total: 76
'''
#-------------------------------------------------------------------------------------------------------------
