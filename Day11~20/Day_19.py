# Find the sum of the digits in the number 100!

# 팩토리얼 100의 모든 자릿수를 합친 값을 구하면 된다.

# 1. 팩토리얼 함수 작성
# 2. string으로 변환 후 map()을 통해 자릿수로 이루어진 map 객체 생성
# 3. sum()을 통해 합을 구한다.

# 팩토리얼 n
def factorial(n):
    result = 1;
    for i in range (n):
        result *= i + 1
    return result

def factorial_digit_sum(n):
    factor = str(factorial(n))
    splited_factor = map(int, factor)
    return sum(splited_factor)

print(factorial_digit_sum(100))