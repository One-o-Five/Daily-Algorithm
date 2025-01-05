# Find the sum of all the primes below two million.

# 200만 이하의 소수를 전부 합하는 문제이다.
# 범위의 소수를 전부 찾아서 리스트로 만들어 준 후 sum()을 활용하자.

primes = []

# 소수인지 확인해주는 함수, 이전에 사용하던 함수에서 while -> for로 수정해보았다.
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 2,000,000 이하의 소수를 전부 list에 추가해준다.
for num in range(2,2000000): # 2,000,000은 소수가 아님
    if isPrime(num) :
        primes.append(num)

print(sum(primes))