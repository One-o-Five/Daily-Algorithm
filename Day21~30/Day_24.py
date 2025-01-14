# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# 피보나치 수열에서 처음으로 1000자리가 되는 것은 몇 항인지 구하는 문제이다.

# 1. 피보나치 수열의 n번째 항을 구하는 함수를 작성.
# 2. 피보나치 수열을 `string`으로 변환해 `length`가 1000 이상이 될때까지 반복문을 거친다.

def fibonacci(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '1'
    elif n > 2 and n % 1 == 0:
        x, y = 1, 1
        for i in range (3, n + 1):
            x, y = y, x + y
        return str(y)
    else:
        return "out of range"

def solution(n):
    i = 0
    # answer = ''
    while len(fibonacci(i)) < n:
        i += 1
        # answer = fibonacci(i)
    # print(answer)
    return i

print(solution(1000))