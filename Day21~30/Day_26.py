
# n^2+an+b, where ∣a∣<1000 and ∣b∣≤1000
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, strating with n=0


# n^2+an+b, where ∣a∣<1000 and ∣b∣≤1000 의 모양을 가진 이차식 중에서 0부터 시작하는 연속된 n에 대해 가장 많은 소수를 만들어내는 이차식을 찾아서, 그 계수 a와 b의 곱을 구하는 문제이다.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True



def solution(x):
    best_length = 0
    result = 0
    
    for a in range (-x, x + 1):
        for b in range (-x, x + 1):
            if (is_prime(b)):
                n = 0
                while True:
                    quad = n**2 + a*n + b
                    if not is_prime(quad):
                        break
                    n += 1
                if n > best_length:
                    best_length = n
                    result = a * b
            else:
                continue
            
    return result

print(solution(1000))