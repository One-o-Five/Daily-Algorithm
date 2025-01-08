"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage.
"""

# 1~1000까지의 숫자를 영어로 표현했을 때 사용한 글자수를 (ex. 342: 'three hundred and forty-two'로 공백과 -는 제외하고 23글자) 전부 구하는 문제이다.

# 1의 자리 (0의 경우 빈 str)
units = [
    "",
    "one", 
    "two", 
    "three", 
    "four", 
    "five", 
    "six", 
    "seven",
    "eight",
    "nine"
    ] 

# 10~19 예외처리용
teens = [
    "ten", 
    "eleven", 
    "twelve", 
    "thirteen", 
    "fourteen", 
    "fifteen", 
    "sixteen", 
    "seventeen", 
    "eighteen", 
    "nineteen"
    ]

# 10의 자리 (0, 1의 경우 빈 str)
tens = [
    "",
    "", 
    "twenty", 
    "thirty", 
    "forty", 
    "fifty", 
    "sixty", 
    "seventy", 
    "eighty",
    "ninety"
    ] 


def to_english(n):
    if 1 <= n < 10: #1~9
        return units[n]
    elif n < 20: #10~19
        return teens[n % 10]
    elif n < 100: #20~99
        ten = tens[n // 10]
        unit = units[n % 10]
        return ten + unit
    elif n < 1000: #100~999
        if n % 100 == 0:
            hundred = units[n // 100] + "hundred"
        else:
            hundred = units[n // 100] + "hundredand"
        ten = (n // 10) % 10
        if ten == 1:
            ten = teens[n % 10]
            unit = ""
        else:
            ten = tens[ten]
            unit = units[n % 10]
        return hundred + ten + unit
    elif n == 1000:
        return "onethousand"
    else:
        return ""

letters = 0
for n in range(1000):
    letters = letters + len(to_english(n+1))

print(letters)
