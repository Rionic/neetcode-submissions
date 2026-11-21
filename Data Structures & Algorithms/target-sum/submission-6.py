class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i, rsum):
            if i == len(nums):
                if rsum == target:
                    return 1
                return 0

            if (i, rsum) in dp:
                return dp[(i, rsum)]
            
            ways = 0

            ways += dfs(i + 1, rsum + nums[i])
            ways += dfs(i + 1, rsum - nums[i])

            dp[(i, rsum)] = ways

            return dp[(i, rsum)]

        return dfs(0, 0)