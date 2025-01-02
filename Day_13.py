"""
The following iterative sequence is defined for the set of positive integers:
n → n / 2 (n is even)
n → 3 n + 1 (n is odd))

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

# 100만 이하의 수로 콜라츠 추측을 진행했을 때. 가장 긴 과정을 거치는 수를 구하는 문제이다.

# 1. for 반복문을 통해 100만 이하의 수를 모두 계산.
# 2. 계산 시 while 반복문을 통해 1이 나올 때 까지 콜라츠 추측을 진행하며 count의 숫자를 1씩 늘린다.

# collatz = []

# for num in range(1, 1000001):
#     n = num
#     count = 0
#     while n != 1:
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             n = 3*n + 1
#         count += 1
#     collatz.append((count, num)); # sort()했을 때 count가 가장 큰 값이 제일 뒤로 갈 수 있게
    
# print(sorted(collatz)[-1])

num = 1
max_count = 0  # 현재까지 가장 긴 변환 횟수
max_num = 0  # max_count를 가진 수

while num <= 1000000:
    n = num
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        count += 1
    if max_count < count:
        print(f"number changed! ({max_num}: {max_count} times -> {num}: {count} times)")
        max_count = count
        max_num = num    
    num += 1

print(f"{max_num}: {max_count} times")
