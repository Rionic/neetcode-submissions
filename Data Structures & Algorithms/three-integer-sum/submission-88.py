class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                numSum = nums[l] + nums[r] + nums[i]
                if numSum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    curR = r
                    r -= 1
                    while r >= 0 and nums[curR] == nums[r]:
                        r -= 1
                elif numSum < 0:
                    l += 1
                else:
                    r -= 1

        return triplets