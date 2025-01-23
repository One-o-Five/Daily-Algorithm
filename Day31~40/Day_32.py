'''
그린닷컴의 운영자 연두는 비밀번호를 평문 그대로 저장하는 과오를 뒤로하고, 이제부터 암호에 해시 함수를 적용해 저장하려고 한다. 
연두가 아는 해시 함수라고는 알고리즘 문제 풀이에 많이 사용되는 롤링 해시 함수밖에 없기 때문에 이것을 응용하여 사용하기로 했다.

그린닷컴의 비밀번호 규칙은 꽤 특이한데, 길이가 정확히 N이어야 하며, 비밀번호를 이루는 문자는 지정된 M개의 문자 중 하나여야 한다. 
따라서, 사용 가능한 각 문자를 0부터 차례대로 정수에 대응시키면, 비밀번호를 길이가 N이고 모든 원소가 0 이상 M-1 이하인 배열 
P = [P(0), P(1), ..., P(N-1)]로 나타낼 수 있다.

이렇게 비밀번호를 배열 P로 나타낸 후, 미리 정해진 정수 A를 이용하여 다음과 같은 해시 함수 h를 적용한다.

h(P) = (P(0) * A^0 + P(1) * A^1 + ... + P(N-1) * A^(N-1)) mod M 

예를 들어 배열 
P = [10, 30, 20], A = 7, M = 55인 경우를 생각해보자. 이 경우 h(P) = (10 * 7^0 + 30 * 7^1 + 20 * 7^2) mod 55 = (10 + 210 + 980) mod 55 = 45$이다. 
여기서 mod는 나머지 연산으로 1200 = 21 * 55 + 45이므로 1200 mod 55 = 45이다. 
따라서 해시값은 항상 0 이상 M-1 이하의 정수이다.

그린닷컴 관리자 계정의 비밀번호 해시값을 해킹한 재현이는, 이 해시값으로 실제 비밀번호가 뭐였는지 역추적해보려고 한다. 
하지만 그린닷컴에서 사용 가능한 비밀번호는 M^N개나 있고, 이 중 과연 알아낸 해시값과 일치하는 비밀번호는 몇 개나 될지 궁금해졌다. 여러분이 이것을 대신 구해주자.

### 입력 ###
첫째 줄에 비밀번호의 길이 N과 문자 종류의 개수 M, 정수 A가 주어진다. (1 ≤ N, M, A ≤ 5,000,000)

둘째 줄에 재현이가 알아낸 해시값 정수 H가 주어진다. (0 ≤ H < M)

### 출력 ###
주어진 해시값을 갖는 비밀번호의 개수를 출력한다. 출력하는 값이 너무 커질 수 있으므로, 이것을 1,000,000,007 ( = 10^9 + 7)로 나눈 나머지를 출력한다.
'''


MOD = 1_000_000_007

def mod_exp(base, exp, mod):
    """빠른 거듭제곱 계산 (base^exp % mod)"""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_passwords(N, M, A, H):
    # A^i % M의 주기 탐색
    mod_powers = []
    current = 1
    seen = {}
    
    for i in range(M):
        if current in seen:
            break
        mod_powers.append(current)
        seen[current] = i
        current = (current * A) % M
    
    # 주기 정보
    cycle_start = seen[current]
    cycle_length = len(mod_powers) - cycle_start

    # A^i % M 계산
    def get_mod_power(i):
        if i < cycle_start:
            return mod_powers[i]
        cycle_index = (i - cycle_start) % cycle_length
        return mod_powers[cycle_start + cycle_index]
    
    # 가능한 해시값 계산
    count = [0] * M
    count[0] = 1  # 초기값

    for i in range(N):
        new_count = [0] * M
        for j in range(M):
            for k in range(M):
                new_hash = (j + k * get_mod_power(i)) % M
                new_count[new_hash] = (new_count[new_hash] + count[j]) % MOD
        count = new_count
    
    return count[H]

# 입력
N, M, A = map(int, input().split())
H = int(input())

# 출력
print(count_passwords(N, M, A, H))
