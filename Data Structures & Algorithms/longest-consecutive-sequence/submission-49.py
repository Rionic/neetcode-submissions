class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numSet = set(nums)
        longest = 1

        for num in nums:
            if num - 1 not in numSet:
                curLen = 1
                while num + curLen in numSet: # Beginning of sequence
                    curLen += 1
                longest = max(longest, curLen)

        return longest