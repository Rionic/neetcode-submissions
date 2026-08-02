class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 1, nums[0]
        minJumps = 1
        # [4, 3, 4, 4, 1, 0, 1, 3, 1]
        #                 l     r
        while l <= r and r < len(nums) - 1:
            bestJump = 0
            while l <= r:
                bestJump = max(nums[l] + l, bestJump)
                l += 1
            r = bestJump
            minJumps += 1

        return minJumps