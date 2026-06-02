class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0] * len(nums)
            else:
                prod *= num

        
        arr = []
        for i, num in enumerate(nums):
            if num == 0:
                arr.append(int(prod))
            elif zeroes < 1:
                arr.append(int(prod/num))
            else:
                arr.append(0)

        return arr       

