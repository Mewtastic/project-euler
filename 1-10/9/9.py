# Find a pythagorean triplet that has a sum of 1000. There is exactly one triplet that meets these conditions.
# I got this on the first DEBUG run of the code!!!
# Built to be effecient in execution, not in lines of code. (Because I thought this would be more CPU intensive :P)
# More than 4 times as effecient as some other more bruted force python solutions!
import math

n1 = 3
n2 = 4

def search(a, b):
    result = None
    search = True
    while search:
        c = math.sqrt(a ** 2 + b ** 2)
        if a + b + c < 1000:
            b += 1
        elif a + b + c > 1000:
            search = False
        else:
            search = False
            result = [a, b, c]

    return result

while True:
    triplets = search(n1, n2)
    if triplets is not None:
        print(math.prod(triplets))
        break
    else:
        n1 += 1
        n2 += 1
