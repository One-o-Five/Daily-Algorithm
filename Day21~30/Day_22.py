# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# 과잉수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합을 구하는 문제이다.

# 1. n의 진약수의 합을 계산해주는 함수를 작성
# 2. n 이하의 모든 과잉수를 찾는 함수를 작성
# 3. 위의 2가지 함수를 활용해 답을 구하는 함수를 작성.

# n의 진약수의 합을 계산
def proper_div_sum(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:  # 제곱근 중복 제거
                divisors.add(n // i)
    divisors.discard(n)
    return sum(divisors)

# n 이하의 모든 과잉수를 찾기
def find_abundant_numbers(n):
    numbers = []
    for i in range (1, n + 1):
        if proper_div_sum(i) > i:
            numbers.append(i)
    return numbers

# n 이하의 과잉수 2개의 합으로 나타낼 수 없는 모든 양의 정수의 합.
def solution(n):
    abundant_numbers = find_abundant_numbers(n)
    abundants_sum = set()
    all_numbers = set(range(1, n + 1))
    
    # 과잉수 두 개의 합으로 나타낼 수 있는 수를 계산
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= n:
                abundants_sum.add(abundant_sum)

    # 과잉수 두 개의 합으로 나타낼 수 없는 수의 합 계산
    non_abundants_sum = all_numbers - abundants_sum
    return sum(non_abundants_sum)

print(solution(28123))