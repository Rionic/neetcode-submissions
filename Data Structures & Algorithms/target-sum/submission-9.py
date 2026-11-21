class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # rsum: ways
        dp = defaultdict(int)
        dp[0] = 1 # (0 sum) -> 1 way

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for curSum, count in dp.items():
                # BELOW IS THE PYRAMID DIAGRAM! 
                # count is the number in the pyramid. dp is prev row, next_dp is cur
                # curSum +/- num is where along the row we place the count! BOOM!
                next_dp[curSum + nums[i]] += count
                next_dp[curSum - nums[i]] += count
            dp = next_dp

        return dp[target] 

        # def dfs(i, rsum):
        #     if i == len(nums):
        #         if rsum == target:
        #             return 1
        #         return 0
        #     if (i, rsum) in dp:
        #         return dp[(i, rsum)]

        #     ways = 0
        #     ways += dfs(i + 1, rsum + nums[i])
        #     ways += dfs(i + 1, rsum - nums[i])

        #     dp[(i, rsum)] = ways
        #     return dp[(i, rsum)]

        # return dfs(0, 0)