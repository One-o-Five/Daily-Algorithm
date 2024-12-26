# What is the 10001st prime number?

# 10001번째 소수를 구하는 문제이다. 
# 소수를 배열에 추가하는 함수를 구현하고, 배열의 길이가 10001이 될때까지 반복해주자.
from time import time

"""
# 소수인지 확인해주는 함수
def isPrime (n):
    if n <= 1: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""

# 유클리드 알고리즘을 이용한 소수인지 확인하는 함수.
def isPrime(n):
	i = 2
	if n <= 1: 
		return False
	while i <= n**0.5:
		if n % i == 0: 
			return False
		i = i + 1
	return True

# n번째 소수를 구하는 함수
def nth_prime (n):
    i = 1
    arr = []
    while len(arr) < n:
        i += 1
        if isPrime(i):
            arr.append(i)
    return i

start = time()
answer = nth_prime(10001)
end = time()

print(f"{answer}, {round(end - start, 5)}sec")