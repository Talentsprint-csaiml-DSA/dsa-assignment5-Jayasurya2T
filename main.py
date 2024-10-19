def min_coins(coins, target_amount):
     # Initialize DP table with infinity for all amounts
    dp = {i: float('inf') for i in range(target_amount + 1)}
    
    # Base case: No coins are needed to make amount 0
    dp[0] = 0

    # Fill the DP table
    for amount in range(1, target_amount + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[target_amount]
