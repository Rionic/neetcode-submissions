class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target = sum(nums)//2
        sums = {0, nums[0]}

        for i in range(1, len(nums)):

            temp = sums.copy()
            for s in sums:
                temp.add(nums[i] + s)
            sums = temp.copy()

        return target in sums
            
