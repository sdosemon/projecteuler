# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers. [done]
# Extra challenge: 
#   Find the largest palindrome made from the product of two, n-digit numbers [done]
#   Find the largest palindrome made from the product of n, 2-digit numbers 
#   Find the largest palindrome made from the product of m, n-digit numbers


# 3-digit numbers:
# largest_palindrome = -1
# for x in range(999,99,-1):
#     for i in range (x,99,-1):
#         if str(x*i) == str(x*i)[::-1]:
#             current_palindrome = x*i
#             if largest_palindrome < current_palindrome:
#                 largest_palindrome = current_palindrome
#                 a = x
#                 b = i

# print(f"{a}*{b} = {largest_palindrome}")

# product of 2, n-digit numbers:
def largest_palindrome(digit_numbers: int):
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

print(largest_palindrome(0))
print(largest_palindrome(1))
print(largest_palindrome(2))
print(largest_palindrome(3))


