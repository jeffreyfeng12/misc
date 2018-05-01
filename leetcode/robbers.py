def robbers(nums):
    dp = [0]*(len(nums) + 2)
    for i in range(len(nums)):
        dp[i+2] = max(dp[i] + nums[i], dp[i+1])
    return dp[len(nums) + 1]
    
print robbers([2,7,9,3,1])