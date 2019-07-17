# Enter a number to determine if it is a prime number.

"""edition 1
value = int(input("Please input a number:"))
isprime = 0

if value <= 1:
    print("It is a wrong number!")
else:
    for i in range(2, value):
        if value % i == 0:
            isprime = 1
            print("It is not a prime number.")
            break
    if isprime == 0:
        print("It is a prime number.")
"""

# edition 2
from math import sqrt

value = int(input("Please input a number:"))
endnum = int(sqrt(value))
isprime = 0

if value <= 1:
    print("It is a wrong number!")
else:
    for i in range(2, endnum + 1):
        if value % i == 0:
            isprime = 1
            print("It is not a prime number.")
            break
    if isprime == 0:
        print("It is a prime number.")