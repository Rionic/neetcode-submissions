class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 1
        l, r = 0, 1

        while r < len(nums) - 1:
            while  r < len(nums) - 1 and nums[l] >= nums[r]:
                r += 1
            if  nums[l] != nums[r] and r - l > 1: # Duplicates detected
                print('dupe', nums[l], nums[r])
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1
                r += 1
        l, r = 0, 1
        while r < len(nums) and nums[l] < nums[r]:
            print(nums[l], nums[r])
            l += 1
            r += 1
        return l + 1
# 2,10,30,10,30,30]
#       l        r