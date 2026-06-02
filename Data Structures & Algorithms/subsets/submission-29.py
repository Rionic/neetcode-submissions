class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # At every point, you either can include or exclude an integer
        res = []

        def backtrack(i, subset):

            # Base case
            if i == len(nums):
                res.append(subset)
                return
            # Exclude number
            backtrack(i + 1, subset)
            # Include number
            backtrack(i + 1, subset + [nums[i]])
            return res

        
        return backtrack(0, [])