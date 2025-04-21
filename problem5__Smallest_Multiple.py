# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (Divisible with no remainder)
# by all of the numbers from 1 to 20?

status = False
for num in range (2520,9144576001,10):
    for i in range(2,21):
        if num % i == 0:
            status = True
        else:
            status = False
            break
    if status == True:
        print(num)
        break

# output -> 232792560

# potential idea to implement: 
# - sieve of eratoshenes (algorithm to find prime up to a given limit)
# - 

        
        

