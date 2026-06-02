class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        for i in range(5):
            print('we are in', l, r)
            m = l + (r-l)//2
            print('m', m)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return -1