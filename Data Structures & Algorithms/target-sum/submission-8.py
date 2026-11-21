class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # rsum: ways
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1 # (0 elements used, sum of 0) -> 1 way
                     # 1 way to sum to zero with first 0 elements
        # 0 elements {0: 1}
        # 1 elements {}
        # 2 elements {}
        # ]

        for i in range(len(nums)):

            for curSum, count in dp[i].items(): 
                # This is dictionary of {sum: way} entries! count = way
                # BELOW IS THE PYRAMID DIAGRAM! 
                # count is the number in the pyramid. i is the pyramid row
                # curSum +/- num is where along the row we place the count! BOOM!
                dp[i + 1][curSum + nums[i]] += count
                dp[i + 1][curSum - nums[i]] += count


        return dp[len(nums)][target] 

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