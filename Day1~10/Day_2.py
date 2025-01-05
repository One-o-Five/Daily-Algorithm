# What is the largest prime factor of the number 600851475143?

# 소인수를 구하려면 어떻게 해야할까?
# 특정 숫자의 약수를 리스트로 출력하는 함수 작성
# 리스트 중에서 소수만을 필터링하는 함수 작성

import time

# listed = []

# # n의 약수를 전부 구하는 함수
# def div (n) :
#     numbers = []
#     for i in range(2, n+1): 
#         if n % i == 0 :
#             numbers.append(i)
#     return numbers

# # n이 소수인지 확인하는 함수
# def isPrime (n):
#     for i in range(2, n):
#         if n % i == 0:
#              return False
#     return True

# # n의 약수들 중에서 소수만 filter 후 list화
# def primes(n) : 
#     return list(filter(isPrime, div(n)))

# def answer(n) : 
#     return primes(n).pop() 



# start_t = time.time()
# print('1000만개', answer(10000000)) #1000만만
# end_t = time.time() - start_t
# print(end_t)

# start_t = time.time()
# print('1억개', answer(100000000)) #1억
# end_t = time.time() - start_t
# print(end_t)

# 위의 방식은 시간복잡도가 너무 높다. 요구받은 숫자를 처리하기 위해서 개선할 필요가 있음.

################################################

# 정수 n을 a*b (a <= b)로 표현할 때 a^2 <= n 이다.
# 정수 n에 대하여 루트n 보다 큰 소인수는 1개 이하이다.
# 즉, 루트n 이하의 숫자만 활용해도 n의 약수와 소인수를 전부 구할 수 있다. 

# 소인수 분해 2
def factorize2(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor <= n**0.5):  # 루트n이하인 숫자까지만
        while (n % factor == 0):  # factor가 n의 소인수라면 전부 나누고 몫을 구한다.
            factors.append(factor)
            n = n // factor  
        factor += 1

    if n > 1 :  # 나올 수 있는 수는 1 또는 소수 뿐이므로, 1이면 버리고 소수면 취한다.
        factors.append(n)
        print(factors)
        return n
    
    print(factors)
    return factor - 1

print(factorize2(600851475143))