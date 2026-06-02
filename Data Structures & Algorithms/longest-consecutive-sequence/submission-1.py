class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = set(nums)
        maxLen = 1
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                curLen = 1
                while num + 1 in nums:
                    num += 1
                    curLen +=1
                if curLen > maxLen:
                    maxLen = curLen

        return maxLen
                
                

