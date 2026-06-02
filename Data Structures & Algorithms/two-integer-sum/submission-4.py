class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            sums[target - num] = i
        # [(4, 0), (3, 1), (2, 2), (1, 3)]
        print(sums)
        for i, num in enumerate(nums):
            if num in sums and i != sums[num]:
                return sorted(list([sums[num], i]))