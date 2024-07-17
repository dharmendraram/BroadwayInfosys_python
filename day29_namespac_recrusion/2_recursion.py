# If a function is called within the definition of the same function then such function
# is called recursive function


# Infinite Recursion
# In such case the code breaks after reaching the maximum recursion depth (~1000)
# def message():
#     print("Hello World")
#     message()
#
# message()


a = 0
def counter():
    global a
    print(a)
    a += 1
    if a <= 10:
        counter()

counter()


# Find the factorial of 5 using:
# i. for loop
# ii. reduce
# iii. recursion

def factorial_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_for_loop(5))


def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)
print(factorial_recursion(5))



from functools import  reduce

# def fxn_reduce(n):
#     return reduce(lambda x,y : x*y, range(1,n+1))
# print(fxn_reduce(5))
#

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


result = factorial(5)
print(result)  # 120


# n * factorial(n-1)
# 5 * factorial(4)  # 5 * 24 = 120
# 4 * factorial(3)  # 4 * 6 = 24
# 3 * factorial(2)  # 3 * 2 = 6
# 2 * factorial(1)  # 2 * 1 = 2
# 1 * factorial(0)  = 1 * 1 = 1