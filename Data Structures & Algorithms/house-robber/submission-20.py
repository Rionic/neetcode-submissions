class Solution:
    def rob(self, nums: List[int]) -> int:
        # [5, 1, 2, 3, 7, 2]
        # [5, 5, 7, 8, 14, 14]
        one, two = 0, 0

        for num in nums:
            three = max(num + one, two)
            one = two
            two = three
            
        return two