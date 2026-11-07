class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Can we start a sequence?
        # set() - traversed unique numbers
        # if num - 1 is in the set, we can add it to cur seq
        # if num - 1 is not in the set, that means it starts a seq

        numset = set()
        for n in nums:
            numset.add(n)
        
        longest = 0

        for i, num in enumerate(nums):
            cur = 0
            while num in numset and num - 1 not in numset:
                numset.remove(num)
                cur += 1
                num += 1
                longest = max(longest, cur)

        return longest