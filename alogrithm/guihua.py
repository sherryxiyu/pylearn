# 最大子数组和
class Solution1:
    def maxSubArray(self, nums) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1]<0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1]+nums[i]
        return max(dp)

#爬楼梯
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        g = [0]*(n+1)
        g[1] = 1
        g[2] = 2
        for i in range(3, n+1):
            g[i] = g[i-1]+g[i-2]
        return g[-1]

def rob(nums) -> int:
    n = len(nums)
    if n<2:
        return nums[0]
    cur, pre = nums[0], 0
    for i in range(n-1):
        cur, pre = max(cur, pre+nums[i+1]), cur
    return cur