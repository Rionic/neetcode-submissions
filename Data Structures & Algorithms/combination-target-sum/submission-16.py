class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            # Current set is larger than target
            # No point to continue adding numbers!
            # Or we hit a leaf node
            if sum(subset) > target or i == len(nums):
                return
            # We found a solution
            if sum(subset) == target:
                res.append(subset[:])
                return
                
            subset.append(nums[i])
            backtrack(i, subset)
            subset.pop()
            # Choose to not reuse current number
            backtrack(i+1, subset)

        backtrack(0, [])
        return res