class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False

        rem = sum(nums) / 2
        # {(i, rem): T/F}
        dp = {}

        def dfs(i, rem):
            if rem == 0:
                return True
            if i == len(nums):
                return False
            
            if (i, rem) in dp:
                return dp[(i, rem)]

            ignore = dfs(i + 1, rem)
            choose = dfs(i + 1, rem - nums[i])

            dp[(i, rem)] = (ignore or choose)
            return dp[(i, rem)]


        return dfs(0, rem)