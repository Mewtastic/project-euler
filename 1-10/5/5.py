# Looking for the smallest number that is evenly divisible by 1-20
# The problem gives us the smallest multiple of 1-10 (2520), so we can just use that to reduce time to solve
search = True
x = 2520

# It's ugly, but it does reduce the number of checks needed...
# Question is does the nested if statements reduce performance enough to make it a bad optimization XD
# With deep regret I report that this abomination is more than twice as fast as my alternate code ;-;
# Perhaps for loops in python are just really ineffecient???
# Or the break isn't working as I anticipated...
while search: # Redundent numbers (4,5,10,2,9,3,1,7) ans: 232792560
    if x % 20 == 0:
        if x % 19 == 0:
            if x % 18 == 0:
                if x % 17 == 0:
                    if x % 16 == 0:
                        if x % 15 == 0:
                            if x % 14 == 0:
                                if x % 13 == 0:
                                    if x % 12 == 0:
                                        if x % 11 == 0:
                                            if x % 8 == 0:
                                                if x % 6 == 0:
                                                    search = False
    if search:
        x += 1

print(x)
