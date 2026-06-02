class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxL = 0

        for num in nums:
            L = 1
            if num - 1 not in nums:
                while num + 1 in nums:
                    num += 1
                    L += 1
            maxL = max(maxL, L)

        return maxL
