from math import gcd
from functools import reduce

def is_curious_fraction(numerator, denominator):
    str_n, str_d = str(numerator), str(denominator)
    if "0" in (str_n[1], str_d[1]):  # 진부한 경우 제외
        return False
    
    for i in range(2):
        for j in range(2):
            if str_n[i] == str_d[j] and str_n[i] != "0":
                reduced_n = int(str_n[1 - i])
                reduced_d = int(str_d[1 - j])
                if reduced_d != 0 and numerator * reduced_d == denominator * reduced_n:
                    return True
    return False

# 조건을 만족하는 분수 찾기
fractions = []
for num in range(10, 100):
    for den in range(num + 1, 100):  # 진분수 조건
        if is_curious_fraction(num, den):
            fractions.append((num, den))

# 분자와 분모의 곱 계산
numerator_product = reduce(lambda x, y: x * y, [num for num, _ in fractions])
denominator_product = reduce(lambda x, y: x * y, [den for _, den in fractions])

# 기약 분수로 변환
common_divisor = gcd(numerator_product, denominator_product)
simplified_denominator = denominator_product // common_divisor

print("조건을 만족하는 분수:", fractions)
print("기약 분수의 분모:", simplified_denominator)
