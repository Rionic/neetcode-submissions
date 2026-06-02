class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0

        for num in nums:
            if num-1 not in nums:
                curLen = 1
                while num + 1 in nums:
                    num += 1
                    curLen += 1
                if curLen > maxLen:
                    maxLen = curLen
                    
        return maxLen
