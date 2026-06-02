class Solution:
    def rob(self, nums: List[int]) -> int:
        # [5, 1, 2, 3, 7, 2]
        # [5, 5, 7, 8, 14, 14]
        if len(nums) < 2: return nums[0]
        rob = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            rob.append(max(nums[i] + rob[i - 2], rob[i - 1]))
            print(i, rob)
            
        return rob[-1]