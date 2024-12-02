#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    fewest_coin_per_index = [float("inf")] * (total + 1)
    fewest_coin_per_index[0] = 0

    dp = fewest_coin_per_index

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[total] if dp[total] != float("inf") else -1
