# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 1~20을 전부 약수로 가지는 가장 작은 숫자를 찾아라. = 1~20의 최소공배수를 찾아라


#### math 모듈을 이용한 방법 ####

import math

numbers = range(1,21)
calculate = math.lcm(*numbers)

for i in numbers :
    if calculate % i == 0 :
        pass
    else :
        print(f"{calculate} can't be divided by {i}")

print(calculate)


#### math 모듈을 이용하지 않는 방법 ####

# 유클리드 알고리즘을 이용한 두 숫자의 최소공배수를 구하는 함수
def LCM(a, b): 
    x, y = a, b
    while y > 0:
        x, y = y, x % y
    GCD = x
    return a * b // GCD 

# 배열에서 순차적으로 최소공배수를 찾아준다 = 배열 속 숫자 전부의 최소공배수를 출력한다.
def LCM_multi(arr):
    x = arr[0]
    for i in arr:
        x = LCM(x, i)
    return x

print(LCM_multi(numbers))