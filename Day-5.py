#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# 1~100 까지의 모든 자연수에 대해 1^2 + 2^2 + ... + 100^2 와 (1+2+3...+100)^2의 차를 구해라.

# for와 range를 이용해서 2개의 변수를 지정해 차를 구하고, 하는김에 숫자의 범위가 변경되도 활용할 수 있도록 구성해보자.

def solution(n):
    squareFirst, sumFirst = 0, 0
    for i in range(1, n+1):
        squareFirst += i**2
        sumFirst += i
    return sumFirst**2 - squareFirst

print(solution(100))