# How many such routes are there through a 20*20 grid? (only being able to move to the right and down)

# 조합을 사용하면 쉽게 답을 구할 수 있을 것이다.
# 경로의 길이는 무조건 오른쪽 20, 아래 20, 총 40으로 나옴.
# 그렇다면 40! / (20!*20!) 을 구하면 된다.

# 팩토리얼
def factorial (n) :
    factor = 1
    for i in range(1, n+1):
        factor *= i
    return factor

# x*y 격자의 길이 몇개인지 출력
def find_routes (x, y):
    routes = factorial(x+y) / (factorial(x) * factorial(y))
    return int(routes)

print(find_routes(20, 20))