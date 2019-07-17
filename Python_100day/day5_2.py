# Looking for "perfect number"
# In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).

print("Perfect number:")
for i in range(1, 10000):
    sum = 0
    for j in range(1, i):
        if 0 == i % j:
            sum += j
    if i == sum:
        print(str(i))

# Perfect number:
# 6
# 28
# 496
# 8128