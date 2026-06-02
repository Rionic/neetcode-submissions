class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                if subset not in res:
                    res.append(subset)
                return

            backtrack(i+1, subset)
            backtrack(i+1, subset + [nums[i]])

            return res

        nums.sort()
        return backtrack(0, [])