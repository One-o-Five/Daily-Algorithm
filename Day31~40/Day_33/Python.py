'''
Coin Sums
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# 영국 화폐 체계에서 동전을 이용해 2파운드를 만드는 조합의 개수를 구하는 문제이다.

# [1, 2, 5, 10, 20, 50, 100, 200] 의 배열을 이용한 점화식을 만들어주자.


def coin_Sums(target, coins):
    dp = [0] * (target + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    return dp[target]

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

print(coin_Sums(target, coins))