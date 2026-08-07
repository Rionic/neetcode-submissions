class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # 8 9 10 11 12 13 14 15 1 2 3 4 5 6 7
        #                       L     M     R
        # t = 3
        # identify sorted side, check if target is within that side.
        # if yes -> update ptrs to sorted side, otherwise rotated side

        while l <= r:
            m = (l + r)//2
            if nums[m] == target: return m
            if nums[r] == target: return r
            if nums[l] == target: return l

            if nums[m] > nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else: 
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1            

        return -1