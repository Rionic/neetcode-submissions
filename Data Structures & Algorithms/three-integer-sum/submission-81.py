class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # -6 0 0 0 3 3 6 6 6 6

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                numSum = nums[l] + nums[r]
                if numSum > -n:
                    # print(n, nums[l],'r',nums[r], numSum,'big')
                    r -= 1
                elif numSum < -n:
                    # print(n, numSum, 'small')
                    l += 1
                else:
                    # print('a')
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r:
                        if nums[l] == nums[l-1]:
                            l += 1
                        elif nums[r] == nums[r+1]:
                            r -= 1
                        else:
                            break
        return res

