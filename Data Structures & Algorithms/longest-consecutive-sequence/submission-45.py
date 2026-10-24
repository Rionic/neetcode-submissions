class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numSet = set(nums)
        longest = 1

        for num in nums:
            # print(numSet)
            if len(numSet) == 0:
                return longest
            curLen = 0
            while num - 1 not in numSet and num in numSet: # Beginning of sequence
                numSet.remove(num)
                curLen += 1
                longest = max(longest, curLen)
                num += 1

        return longest