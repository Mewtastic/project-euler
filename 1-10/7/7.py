# 10,001st prime... A useful algorithm to start off code breaking I suppose? Idk, I'm not a Cryptographer.
# I originally set search to a ridiculous 100,020,001 just to be sure.
# Afterword I set the number to be just above where I originally found the prime to see how fast I could get the answer.
# Initial solve 7 seconds, second go 0.021 miliseconds

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

search = 105000
ans = sieve(search)

print("Answer: " + str(ans[10000]))
print("Primes found: " + str(len(ans)))
