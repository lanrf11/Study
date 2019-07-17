# "One hundred dollars to buy a hundred chickens" problem ——Chinese ancient arithmetic problem
# One cock costs 5, one hen costs 3, three chicks cost 1.
# One hundred dollars to buy a hundred chickens.
# Calculate the number of cock, hen, chick.

n = 1
print("The result is:")
for cock in range(0, int(100/5)+1):
    for hen in range(0, int((100 - 5 * cock)/3) + 1):
        chick = (100 - 5 * cock - 3 * hen) * 3
        if cock + chick + hen == 100:
            print(str(n) + ". Cock:" + str(cock) + ", chick:" + str(chick) + ", hen:" + str(int(hen)))
            n = n + 1

# The result is:
# 1. Cock:0, chick:75, hen:25
# 2. Cock:4, chick:78, hen:18
# 3. Cock:8, chick:81, hen:11
# 4. Cock:12, chick:84, hen:4
