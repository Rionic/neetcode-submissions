class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, subset):
            # Base case
            if i == len(nums):
                result.append(subset[:])
                return

            # Exclude current num
            backtrack(i + 1, subset)
            # Include current num
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

        backtrack(0, [])

        return result
