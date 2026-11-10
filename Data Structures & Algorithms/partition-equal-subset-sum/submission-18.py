class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        target = s // 2
        sums = set()
        sums.add(0)

        for i in range(len(nums)):
            
            subset = set()
            for t in sums:
                subset.add(t + nums[i])
            sums |= subset

        return target in sums
