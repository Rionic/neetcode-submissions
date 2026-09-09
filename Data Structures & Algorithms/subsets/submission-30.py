class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subs = []

        def backtrack(sub, i, nums):
            if i == len(nums):
                subs.append(sub)
                return

            backtrack(sub.copy(), i + 1, nums)
            sub.append(nums[i])
            backtrack(sub.copy(), i + 1, nums)

        backtrack([], 0, nums)


        return subs