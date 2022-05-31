#Write your code below this line 👇

#prime number (or a prime) is a natural number greater than 1 
# that is not a product of two smaller natural numbers. 
# A natural number greater than 1 that is not prime is called a composite number. 
#For example, 
# 5 is prime because the only ways of writing it as a product, ARE 1 × 5 or 5 × 1, involve 5 itself. 
# However, 4 is composite because it is a product (2 × 2) in which both numbers are 
# smaller than 4.

# "A PRIME NUMBER IS ONLY DIVISIBLE BY 1 OR ITSELF." 

import os

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
            print(f'{number} is prime')
    else:
            print(f'{number} is not a prime.')


    print()

os.system(' clear ')
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)