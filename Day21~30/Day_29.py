# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# 각 자리 숫자를 5제곱해서 더했을 때 자기 자신이 되는 수들의 합을 구하는 문제이다.

# 1. 각 자리의 숫자를 5제곱해서 더했을 때의 최대값을 구해보면 6자리 까지만 찾아보면 됨을 알 수 있다.
# 2. 그 합의 범위에서 반복문을 돌려준다.

# 각 자리 숫자를 5제곱해서 더했을 때 자기 자신이 되는 수를 찾는 함수
def digit_fifth_powers():
    numbers = []

    # 1부터 9^5 * 6 (6자리 수 최대값)까지 확인
    upper_limit = 9**5 * 6
    for num in range(2, upper_limit):
        digit_sum = 0
        
        for digit in str(num):
            digit_sum += int(digit)**5
        
        if num == digit_sum:
            numbers.append(num)
    
    return sum(numbers)

print(digit_fifth_powers())