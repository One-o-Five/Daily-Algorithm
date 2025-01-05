# 400만 이하의 피보나치 수열 중 짝수의 합을 구하라
fib = []
even_fib = []
sum_even_fib = 0

def func(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    for i in range(1, n):
        a, b = b, a+b
    return a

i = 0
while func(i) <= 4000000:
    i = i+1
    fib.append(func(i))
    if func(i) % 2 == 0:
        sum_even_fib += func(i)
        # even_fib.append(func(i))


# x, y = 0, 0
# while y <= 4000000:
#     if y == 0:
#         x, y = 1, 1
#         fib = [1, 1]
#     x, y = y, x+y
#     fib.append(y)
#     if y % 2 == 0 :
#         even_fib.append(y)
#         sum_even_fib += y

        
print(fib)
print(even_fib)
print(sum_even_fib)
