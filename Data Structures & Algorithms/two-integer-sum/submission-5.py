class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            if num in sums:
                return sorted(list([sums[num], i]))
            sums[target - num] = i
