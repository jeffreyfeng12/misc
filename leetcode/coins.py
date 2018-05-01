def coins(amount, coins):
    dp = [0]*(amount + 1)
    for i in coins: dp[i] = 1
    for i in range(amount + 1):
        for j in range(1, i/2 + 1):
            print j, dp[j], dp[i-j]
            #print j, dp[j], dp[i - j]
            dp[i] += dp[j] * dp[i-j]
        print i, dp

    return dp[amount]
    
    
print coins(8, [2, 3, 5])