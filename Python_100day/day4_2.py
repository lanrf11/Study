# Enter two positive integers to calculate the greatest common divisor and the least common multiple.

num1 = int(input("Please input the first positive integer:"))
num2 = int(input("Please input the second positive integer:"))

bignum = max(num1, num2)
smallnum = min(num1, num2)
isfindgcd = 0

for i in range(smallnum, 1, -1):
    if num1 % i == 0 and num2 % i == 0:
        isfindgcd = 1
        print("The greatest common divisor is " + str(i))
        break
if isfindgcd == 0:
    print("They do not have the greatest common divisor.")

for i in range(bignum, num1*num2+1):
    if i % num1 == 0 and i % num2 == 0:
        print("The least common multiple is " + str(i))
        break
