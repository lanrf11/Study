# Looking for "Daffodil Number"
# A daffodil number is a three-digit number whose value is equal to the sum of cubes of each digit.
# For example. 153 is a daffodil as 153 = 1**3 + 5**3 + 3**3.

# attention:
# 10 / 3 = 3.333333333333333
# 10 // 3 = 3
# 10 % 3 = 1

print("Daffodil Number:")
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if i == a**3 + b**3 + c**3:
        print(str(i))

# Daffodil Number:
# 153
# 370
# 371
# 407