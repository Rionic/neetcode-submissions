class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                if subset not in res:
                    res.append(subset[:])
                return []

            backtrack(i+1, subset)
            subset.append(nums[i])
            sortset = sorted(subset)
            backtrack(i+1, sortset)
            subset.pop()

            return res

        return backtrack(0, [])