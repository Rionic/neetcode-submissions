class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1: return False
        final = set()

        for i in range(len(nums)):
            temp = set()
            for n in final:
                if nums[i] + n > sum(nums) / 2:
                    continue
                temp.add(nums[i] + n)

            final.add(nums[i])
            final |= temp
        print(final,sum(nums))
        return sum(nums) / 2 in final

