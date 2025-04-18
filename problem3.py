# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def largest_prime_factor(value):
    for i in range(1,value):
        x = value-i
        if value % x != 0:
            continue
        else:
            status = False
            for num in range(2,x):
                if x % num != 0:
                    status = True
                    continue
                else:
                    status = False
                    break
            if status == True:
                return x
                    
                
print(f"the largest prime factor is {largest_prime_factor(600851475143)}")

