# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# 과잉수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합을 구하는 문제이다.

# n의 진약수의 합을 계산
def get_divisors_sum(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

# limit 이하의 모든 과잉수를 찾기
def find_abundant_numbers(limit):
    return [n for n in range(1, limit + 1) if get_divisors_sum(n) > n]

def non_abundant_sum(limit):
    abundant_numbers = find_abundant_numbers(limit)
    abundant_sums = set()
    
    # 과잉수 두 개의 합으로 나타낼 수 있는 수를 계산
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                abundant_sums.add(abundant_sum)
            else:
                break

    # 과잉수 두 개의 합으로 나타낼 수 없는 수의 합 계산
    all_numbers = set(range(1, limit + 1))
    non_abundant_sums = all_numbers - abundant_sums
    return sum(non_abundant_sums)

# 결과 출력
result = non_abundant_sum(28123)
print(result)