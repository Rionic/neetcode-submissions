class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        product = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes+=1
                if zeroes > 1:
                    product = 0
                    break
                continue
            product *= num

        for num in nums:
            if num == 0:
                output.append(product)
            elif zeroes == 1:
                output.append(0)
            else:
                output.append(int(product/num))

        return output
