class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = []
        # [6, 7, 1, 2, 3, 4, 5]
        while l <= r:
            print(l, r)
            if nums[l] < nums[r]: # We are at the smallest element!
                if res == []:
                    return nums[l]
                return min(res[-1], nums[l])
            m = (l + r)//2
            if nums[m] >= nums[l]: # Answer is to the right!
                if res == [] or res[-1] > nums[m]:
                    res.append(nums[m])
                l = m + 1
            else: # Answer is to the left!
                if res == [] or res[-1] > nums[m]:
                    res.append(nums[m])
                r = m - 1

        return res[-1]