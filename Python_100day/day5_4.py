# Fibonacci sequence
# F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

ENDNUMBER = 20

def Fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return Fibonacci(i-1) + Fibonacci(i-2)

for i in range(1, ENDNUMBER + 1):
    print("Fibonacci(" + str(i) + ")=" + str(Fibonacci(i)))

"""
Fibonacci(1)=1
Fibonacci(2)=1
Fibonacci(3)=2
Fibonacci(4)=3
Fibonacci(5)=5
Fibonacci(6)=8
Fibonacci(7)=13
Fibonacci(8)=21
Fibonacci(9)=34
Fibonacci(10)=55
Fibonacci(11)=89
Fibonacci(12)=144
Fibonacci(13)=233
Fibonacci(14)=377
Fibonacci(15)=610
Fibonacci(16)=987
Fibonacci(17)=1597
Fibonacci(18)=2584
Fibonacci(19)=4181
Fibonacci(20)=6765
"""