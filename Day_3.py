# A palindromic number reads the same both ways.  
# The largest palindrome made from the product of two 2-digit numbers is 
# 9009 = 91 * 99

# Find the largest palindrome made from the product of two 3-digit numbers

# 3자리 숫자 2개의 곱으로 만들수 있는 가장 큰 palindrome number 구하기

# 1.  우선 두 정수 a, b를 3자리로 제한하고
# 2. palindrome 인지 확인하는 함수를 만든다.
# 3. 그 후에 a와 b의 곱을 전부 구해서 palindrome라면 list에 추가한다.
# 4. 정렬 후에 list.pop()을 통해 가장 큰 수를 출력한다.

a = 100
palindromes = []

def isPalindrome (n) :
    reverse_num = 0
    num = n
    while num > 0:             
        remainder = num % 10    # 1의 자리를 구한 후 
        reverse_num = reverse_num * 10 + remainder  # reverse_num에 더한 후 10을 곱하는 것을 반복 
        num = num // 10   # 10으로 나눈 후의 1의 자리 수 = 다음 자릿 수 구하기
    if reverse_num == n:
        return True
    return False

while a < 1000 :
    b = 100  # a가 1 커질때 마다 100 부터 다시 시작해야 함
    while b < 1000:
        if isPalindrome(a*b) :
            palindromes.append((a*b, a, b))  # N = a * b 형태의 답으로 출력하고 싶다.
        b += 1
    a += 1

largest = sorted(palindromes).pop()
answer = f"{largest[0]} = {largest[2]} * {largest[1]}"

print(answer)