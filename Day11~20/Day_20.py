# Evaluate the sum of all the amicable numbers under 10000

# 10000 이하의 친화수를 모두 찾아서 그 합을 구하는 문제이다.

# 1. n의 진약수를 모두 구해 그 합을 출력해주는 함수를 작성
# 2. n이 친화수에 포함되는지 확인해주는 함수를 작성
# 3. n 이하의 모든 진약수를 합해주는 함수를 작성.

def proper_divs(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:  # 제곱근 중복 제거
                divisors.add(n // i)
    divisors.discard(n)
    return sum(divisors)

def is_amicable(n):
    couple = proper_divs(n)
    if couple != n and proper_divs(couple) == n:
        return True
    else:
        return False
    
def solution(n):
    result = 0
    for i in range(1, n +1):
        if is_amicable(i):
            result += i
    return result

print(solution(10000))
