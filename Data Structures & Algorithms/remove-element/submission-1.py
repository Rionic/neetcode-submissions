class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                j += 1
        
        nums.sort(reverse=True)

        return len(nums) - j
