# This problem is more of a toungue twister than a problem
squares = 0
sum = 0

for i in range(1, 101):
    sum += i
    squares += i**2

sum = sum**2

print(sum-squares)
