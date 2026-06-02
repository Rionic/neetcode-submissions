class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums = set(nums)
        subsets = []
        subset = []

        def dfs(i): # i tells use which element we're currently visiting
            if i >= len(nums):
                subsets.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i]) 
            dfs(i + 1)

            # decision to exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return subsets
            

