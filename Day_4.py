# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 1~20을 전부 약수로 가지는 가장 작은 숫자를 찾아라. = 1~20의 최소공배수를 찾아라

import math

numbers = range(1,21)
calculate = math.lcm(*numbers)

for i in numbers :
    if calculate % i == 0 :
        pass
    else :
        print(f"{calculate} can't be divided by {i}")

print(calculate)