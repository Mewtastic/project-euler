n0 = 1
n1 = 2

sum = 2

while n1 <= 4000000:
    x = n0 + n1
    if x % 2 == 0:
        sum += x
    n0 = n1
    n1 = x

print(sum)
