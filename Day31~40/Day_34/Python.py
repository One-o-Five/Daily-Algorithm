# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39×186=7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# 1~9 팬디지털 곱셈식을 만들 수 있는 모든 수의 합을 구하는 문제이다.

# 각 숫자를 String으로 변환 후 더해주면 바로 모든 조합을 확인해볼 수 있을 것 같다.
# 우선 10000 * 10000 부터는 c가 10자리가 되어버리니 a와 b의 범위는 4자리 수 이하
# 이중반복문을 통해 구현해보자.

def pandigital_products():
    temp_set = set()  # 중복값 제거를 위해 set으로 초기화
    for a in range(10000):
        for b in range(10000):
            if len(str(a))+len(str(b))+len(str(a*b))>9:  # a, b, c의 자릿수의 합이 이미 9보다 클 경우 더 찾아도 의미 없으니 break
                break
            if len(str(a))+len(str(b))+len(str(a*b))==9: 
                s=sorted(str(a)+str(b)+str(a*b))
                if s==['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    temp_set.add(a*b)
    
    return sum(temp_set)
                
print(pandigital_products())