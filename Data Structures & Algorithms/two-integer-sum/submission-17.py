class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(int)
        for i, n in enumerate(nums):

            if n in numMap:
                return [numMap[n], i]
            numMap[target - n] = i

