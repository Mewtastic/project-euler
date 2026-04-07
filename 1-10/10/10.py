# And this is why we did overkill on problem 7! Now it's super easy to solve 10

def sieve(num):
    primes = [True] * (num + 1)
    x = 2
    while x ** 2 <= num:
        if primes[x]:
            for i in range(x ** 2, num + 1, x): # Multiples of x are not primes
                primes[i] = False
        x += 1
    ans = []
    for x in range(2, num + 1):
        if primes[x]:
            ans.append(x)
    
    return ans

search = 2000000
ans = sieve(search)

print("Answer: " + str(sum(ans)))
print("Primes found: " + str(len(ans)))
