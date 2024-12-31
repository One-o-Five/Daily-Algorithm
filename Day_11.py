# What is the value of the first triangle number to have over five hundred divisors?

# 500개 이상의 약수를 갖는 가장 작은 삼각수를 구하는 문제이다.

# 1. n의 약수가 몇개인지 출력하는 함수를 작성한다.
# 2. 약수가 n개 이상일 때까지 삼각수를 구하는 함수를 작성한다.

# 약수의 개수를 구하는 함수
def count_div(n):
    divisors = set() # n의 정수의 제곱일 경우 중복 값이 나오니 set()을 활용.
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return len(divisors)

# 삼각수 구하기
def find_tri_div(n):
    i = 1
    tri_num = 0
    
    while True:
        tri_num += i
        if count_div(tri_num) > n:
            return tri_num
        i += 1

# 500개 이상의 약수를 갖는 삼각수 찾기
result = find_tri_div(500)
print(result)