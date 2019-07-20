# Task1: Find the greatest common divisor and the least common multiple.
def GCDandLCM(x, y):
    num_min = min(x ,y)
    num_max = max(x, y)
    for i in range(num_min, 0, -1):     # range(5, 0, -1):5, 4, 3, 2, 1.
        if x % i == 0 and y % i == 0:
            lcd = i
            break
    lcm = int(num_max / lcd * num_min)
    return lcd, lcm


# Task2: Determine if a number is a palindrome.
def isPalindrome(x):
    x = str(x)
    flag = 0
    len_x = len(x)
    if len_x == 1:
        flag = 1
    else:
        flag = 1
        for i in range(0, len_x//2 + 1):
            if x[i] != x[len_x-i-1]:
                flag = 0
                break
    return flag

def isPalindrome2(x):
    num_reverse = 0
    temp = x
    while temp > 0:
        num_reverse = num_reverse * 10 + temp % 10
        temp //= 10
    return num_reverse == x


# Task3: Determine if a number is a prime number.
def isPrime(x):
    flag = 1
    if x == 1:
        flag = 0
    for i in (2, int(x ** 0.5) + 1):
        if x % i == 0:
            flag = 0
            break
    return flag

# Task4: Determine whether the input positive integer is a palindrome prime number.
def isPalindromeAndPrime(x):
    if isPalindrome(x) == 1 and isPrime(x) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    # x = 3
    # y = 3
    # lcd, lcm = GCDandLCM(x, y)
    # print(lcd, lcm)
    
    # x2 = 1
    # y2 = 12321
    # z2 = 15676521
    # isPal1 = isPalindrome(x2)
    # isPal2 = isPalindrome(y2)
    # isPal3 = isPalindrome(z2)
    # print(isPal1, isPal2, isPal3)
    # isPal11 = isPalindrome2(x2)
    # isPal21 = isPalindrome2(y2)
    # isPal31 = isPalindrome2(z2)
    # print(isPal11, isPal21, isPal31)

    # x3 = 1
    # y3 = 6
    # z3 = 59
    # print(isPrime(x3))
    # print(isPrime(y3))
    # print(isPrime(z3))

    x4 = 11
    y4 = 66
    z4 = 12344321
    print(isPalindromeAndPrime(x4))
    print(isPalindromeAndPrime(y4))
    print(isPalindromeAndPrime(z4))