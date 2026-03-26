# This code SUCKS! The answer is found almost instantly, but it does a HUGE load of computing afterwards that does NOTHING!
# TODO: Make it better while proving beyond a reasonable doubt that 6857 is the correct answer.
x = 600851475143
result = 0

def isPrime(y):
    prime = True
    for i in range(2, int(y*.5)+1):
        if y % i == 0:
            prime = False
            break
    
    return prime

for i in range(3, 300425737572):
    if x % i == 0:
        if isPrime(i) is True: 
            result = i
            print(result)

print(result)
