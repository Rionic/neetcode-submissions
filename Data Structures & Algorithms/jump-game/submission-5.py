class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        jumps = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                jumps += 1
            elif jumps > 0:
                jumps +=1
                if nums[i] >= jumps or i + nums[i] >= len(nums) - 1:
                    print(nums[i], 'jumped at i =', i )
                    jumps = 0
        print(jumps)
        return jumps == 0
