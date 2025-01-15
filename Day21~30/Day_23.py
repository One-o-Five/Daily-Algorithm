# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서 1,000,000번째를 구하는 문제다.

'''from itertools import permutations

# 0~9까지 모든 사전식 순열을 만들어준다
digits = '0123456789'
all_permutations = sorted(permutations(digits))

# 1,000,000 째 숫자를 조합해서 출력한다,
millionth_permutation = ''.join(all_permutations[999999])

print(millionth_permutation)
'''

def factorial(n):
    result = 1;
    for i in range (n):
        result *= i + 1
    return result

def nth_permutation(n):
    target = n
    digits = list(range(10))
    result = []
    
    # 9!부터 0까지 1씩 줄여나간다.
    for i in range(len(digits) - 1, -1, -1):
        factor = factorial(i)
        index = target // factor
        result.append(digits.pop(index))  # 고른 숫자는 빼야하니
        target = target % factor
    
    return ''.join(map(str, result)) # result의 값을 str으로 변환 후 join

print(nth_permutation(999999))