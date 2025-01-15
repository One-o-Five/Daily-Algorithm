# Find the value of 'd < 1000' for which '1/d' contains the longest recurring cycle in its decimal fraction part.

# 1000 이하의 자연수 d 중에서 $1/d$ 를 소수로 표현했을 때 가장 긴 순환마디를 갖는 수를 구하는 문제이다.

# 1. 소수 첫번째 숫자와 같은 숫자가 나올 때 마다 직전 까지의 숫자와 그 이후의 숫자가 같은지 확인해주는 방식으로 $1/d$ 의 순환 마디를 구하는 함수를 작성해준다.
# 2. 1000 이하의 모든 자연수를 대입하여 순환마디가 가장 긴 수를 찾는다.

def recurring_cycle_length(d):
    remainder = 1
    seen_remainders = {}
    position = 0

    while remainder != 0:
        if remainder in seen_remainders:
            return position - seen_remainders[remainder]
        seen_remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1

    return 0

def reciprocal_cycle(d):
    max_length = 0
    longest_number = 0
    
    for i in range(1, d):
        length = recurring_cycle_length(i)
        if length > max_length:
            max_length = length
            longest_number = i
    
    return (f"d = {longest_number}, length = {max_length}")
    
print(reciprocal_cycle(1000))