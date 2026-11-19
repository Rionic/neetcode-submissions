class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}

        def dfs(i, s):
            if i == len(nums):
                if s == target: return 1
                return 0

            if (i, s) in dp:
                return dp[(i, s)]

            sums = 0
            sums += dfs(i + 1, s + nums[i])
            sums += dfs(i + 1, s - nums[i])
            dp[(i, s)] = sums

            return dp[(i, s)]

        return dfs(0, 0)