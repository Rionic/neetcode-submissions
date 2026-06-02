class Solution:
    def rob(self, nums: List[int]) -> int:
        # These are essentially filler values prepending the array
        # 0 0 [1 2 3 1]
        # They natrually get incremented in the loop
        one, two = 0, 0

        for num in nums:
            three = max(num + one, two)
            one = two
            two = three
            
        return two
            
