# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# def largest_prime_factor(value):
#     for i in range(1,value):
#         x = value-i
#         if value % x != 0:
#             continue
#         else:
#             status = False
#             for num in range(2,x):
#                 if x % num != 0:
#                     status = True
#                     continue
#                 else:
#                     status = False
#                     break
#             if status == True:
#                 return x
# ^ not memory efficient enough

import math

def largest_prime_factor(n):
    max_prime = -1

    #   Strip out factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    #    Now n is odd. Try odd divisors from 3 up to sqrt(n)
    #    Each time we find a divisor, divide it out completely.
    for d in range(3, int(math.isqrt(n)) + 1): 
        # while factoring any n as 
        #   a x n = b with a <= b
        # then a <= sqrt(n) and b >= sqrt(n)
        #   only need to test for divisor up to sqrt(n) 
        #   since all divisor b has been captured by 'pair' divisor a
        while n % d == 0:
            max_prime = d
            n //= d

    #   If what's left is > 2, it's a prime larger than any we found
    if n > 2:
        max_prime = n

    return max_prime

print(largest_prime_factor(5))
print(largest_prime_factor(49))
print(largest_prime_factor(121))
print(largest_prime_factor(169))
print(largest_prime_factor(2**10))
print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))