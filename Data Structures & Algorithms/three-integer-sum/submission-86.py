class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []
        i = prevI = 0
        print(nums)
        while i < len(nums):
            if i != 0 and nums[i] == nums[prevI]:
                i += 1
                continue
            print('i is', nums[i])
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
            prevI = i
            i += 1

        return triplets