numbers = 0

for i in range(3,1000):
    if i % 3 == 0:
        numbers += i
    elif i % 5 == 0:
        numbers += i

print(numbers)
