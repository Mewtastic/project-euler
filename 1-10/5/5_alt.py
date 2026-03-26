# Looking for the smallest number that is evenly divisible by 1-20
# The problem gives us the smallest multiple of 1-10 (2520), so we can just use that to reduce time to solve
search = True
x = 2520

while search:
    x += 1
    search = False
    for i in range(20, 6, -1):
        if x % i != 0:
            search = True
            break

print(x)
