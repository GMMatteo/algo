# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.
# def sigma(n):
#     if n <= 0:
#         return 0
#     return sigma(n-1) + n

# x = sigma(5)
# print(x)

def sigma(n):
    if n > 0:
        return sigma(n-1) + n
    return 0
x = sigma(5)
print(x)
 


# Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).
# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n-1)

# y = factorial(3)
# print(y)

def factorial(num):
    if num > 1:
        return factorial(num-1) * num
    return 1

y = factorial(6)
print(y)