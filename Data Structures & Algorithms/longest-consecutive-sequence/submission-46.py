class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numSet = set(nums)
        longest = 1

        for num in nums:
            if len(numSet) == 0: return longest
            if num - 1 not in numSet:
                curLen = 0
                while num in numSet: # Beginning of sequence
                    numSet.remove(num)
                    curLen += 1
                    longest = max(longest, curLen)
                    num += 1

        return longest