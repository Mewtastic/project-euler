largest_product = 0

def isPalindrome(num):
    palindrome = False
    digits = len(str(num))
    reverse = 0
    for i in range(0, digits):
        y = num % 10
        num = int(num / 10)
        reverse = reverse * 10 + y
    if product == reverse:
        palindrome = True

    return palindrome

for i in range(100, 1000):
    for z in range(100, 1000):
        product = i*z
        if product > largest_product:
            if isPalindrome(product):
                largest_product = product

print(largest_product)
