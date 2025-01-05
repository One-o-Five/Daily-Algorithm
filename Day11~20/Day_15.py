
# What is the sum of the digits of the number 2^1000?

def solution (n):
    string = str(2**n)
    mapping = map(int, string)
    result = sum(mapping)
    return result

result = sum([int(i) for i in str(2**1000)])

print(solution(1000))
print(result)