'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24  25
20  7  8  9  10
19  6  1  2  11
18  5  4  3  12
17 16 15 14  13
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# 위의 나선 행렬과 같은 방식으로 1001*1001 행렬을 만들었을 때 대각선 상의 수를 모두 더한 값을 구하는 문제이다.

def solution(n):
    diagonals_sum = 1 # 합한 값
    last_number = 1 # 이전 행렬의 마지막 숫자 기록용
    # 3 ~ n까지 홀수만
    for i in range (3, n + 1, 2):
        for j in range(4):
            last_number += i - 1
            diagonals_sum += last_number
                
    return diagonals_sum

print(solution(1001))

# def solution(n):	
#     diagonals_sum = 1
#     for i in range (3, n  + 1, 2):
#         result+=4*i**2 - 6*(i-1)
#     return diagonals_sum

# print(solution(1001))