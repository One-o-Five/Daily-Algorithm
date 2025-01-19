# How many distinct terms are in the sequence generated by a^b for 2≤a≤100 and 2≤b≤100?

# 2≤a≤100 이고 2≤b≤100 인 a, b를 가지고 만들 수 있는 a^b 중에서 중복값 제외한 개수를 구하는 문제이다.


def distinct_powers(n):
    distinct_terms = set()
    numbers = range(2, n + 1)

    for a in numbers:
        for b in numbers:
            distinct_terms.add(a**b)
            
    return len(distinct_terms)

print(distinct_powers(100))