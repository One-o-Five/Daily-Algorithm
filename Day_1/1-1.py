# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 
# 이들의 총합은 23이다.
# 1,000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.


# 1. 3의 배수와 5의 배수를 전부 리스트 한다.
# 2. 3과 5의 공배수(=중복되는 숫자)는 1번 제거한다.
# 3. 리스트를 전부 합친다, sum을 사용하면 됨.

# third = [] # 3의 배수의 리스트
# fifth = [] # 5의 배수의 리스트

# for i in range(1, 1000):
#     if i % 3 == 0 :
#         third.append(i)  

# for i in range(1, 1000):
#     if i % 5 == 0 :
#         fifth.append(i) 

# filtering = list(set(third + fifth)) # 리스트 2개를 합쳐서 중복 값을 제거 (list -> data -> list)
# answer = sum(filtering)  # 중복값이 사라진 리스트의 값을 전부 합침침

# print(answer)

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0: 
        result += n
        
print(result)