# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers. [done]
# Extra challenge: 
#   Find the largest palindrome made from the product of two, n-digit numbers [done]
#   Find the largest palindrome made from the product of n, 2-digit numbers 
#   Find the largest palindrome made from the product of m, n-digit numbers


# 3-digit numbers:

largest_palindrome_2_3 = -1
for x in range(999,99,-1):
    for i in range (x,99,-1):
        if str(x*i) == str(x*i)[::-1]:
            current_palindrome = x*i
            if largest_palindrome_2_3 < current_palindrome:
                largest_palindrome_2_3 = current_palindrome
                a = x
                b = i

print(f"{a}*{b} = {largest_palindrome_2_3}")


# product of 2, n-digit numbers:

def largest_palindrome_2_n(digit_numbers: int):
    if not digit_numbers:
        return "You are silly!"

    largest_palindrome = -1
    if digit_numbers == 1:
        max_value = 9
        min_value = 0
    else:
        max_value = int("9"*digit_numbers)
        min_value = int("9"*(digit_numbers-1))
        
    for x in range(max_value,min_value,-1):
        for i in range (x,min_value,-1):
            if str(x*i) == str(x*i)[::-1]:
                current_palindrome = x*i
                if largest_palindrome < current_palindrome:
                    largest_palindrome = current_palindrome
                    a = x
                    b = i
    return (f"{a}*{b} = {largest_palindrome}")

print(largest_palindrome_2_n(0))
print(largest_palindrome_2_n(1))
print(largest_palindrome_2_n(2))
print(largest_palindrome_2_n(3))


# product of n, 2-digit numbers:

def recursion_n_2(n, base = 10):

    if n == 0:
        yield []
    else:
        for i in range(99, base - 1, -1):
            for tail in recursion_n_2(n-1, base):
                yield [i] + tail


def largest_palindrome_n_2(products: int):
     
     if not products:
         return [] 
    
     largest_palindrome = -1
     factors = []

     for combination in recursion_n_2(products):
         product_comb = 1
         for num in combination:
             product_comb *= num
         s = str(product_comb)
         if s == s[::-1] and product_comb > largest_palindrome:
             largest_palindrome = product_comb
             factors = combination[:]

     return largest_palindrome, factors
            
     
print(largest_palindrome_n_2(2))
print(largest_palindrome_n_2(3))
print(largest_palindrome_n_2(4))
print(largest_palindrome_n_2(1))
print(largest_palindrome_n_2(0))


# product of n, n-digits numbers:

def recursion_n_n(n, x, y):

    if n == 0:
        yield []
    else:
        for i in range(x,y, -1):
            for tail in recursion(n-1,x, y):
                yield [i] + tail


def largest_palindrome_n_n(products: int, digits: int):
     
     if not products:
         return [] 
    
     upper = int("9" * digits)
     if digits == 1:
         lower = 0
     else:
         lower = int("9" * (digits - 1))
     largest_palindrome = -1
     factors = []

     for combination in recursion_n_n(products, upper, lower):
         product_comb = 1
         for num in combination:
             product_comb *= num
         s = str(product_comb)
         if s == s[::-1] and product_comb > largest_palindrome:
             largest_palindrome = product_comb
             factors = combination[:]

     return largest_palindrome, factors

print(largest_palindrome_n_n(3,1))
print(largest_palindrome_n_n(0,0))
print(largest_palindrome_n_n(1,1))
print(largest_palindrome_n_n(2,2))
print(largest_palindrome_n_n(3,3))