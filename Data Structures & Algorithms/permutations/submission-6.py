class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        numlen = len(nums)
        def backtrack(perm, nums):
            # Base case
            if len(perm) == numlen:
                res.append(perm[:])
            # Backtrack step 
            for i, n in enumerate(nums):
                perm.append(n)
                nums.pop(i)
                backtrack(perm, nums)
                perm.pop()
                nums.insert(i, n)

        backtrack([], nums)
        return res