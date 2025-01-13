# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서 1,000,000번째를 구하는 문제다.

from itertools import permutations

# 0~9까지 모든 사전식 순열을 만들어준다
digits = '0123456789'
all_permutations = sorted(permutations(digits))

# 1,000,000 째 숫자를 조합해서 출력한다,
millionth_permutation = ''.join(all_permutations[999999])

print(millionth_permutation)