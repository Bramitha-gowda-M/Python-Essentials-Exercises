#A series of number in which each number is the sum of the two preceding numbers.
# 0, 1, 1, 2, 3, 5

fib1 = 0
fib2 = 1

print(fib1)
print(fib2)

for i in range(2,10):
    fib = fib1 + fib2
    print(fib)
    fib1 = fib2
    fib2 = fib
    