class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(self.robSub(nums[:-1]), self.robSub(nums[1:]), nums[0])
        
    def robSub(self, a):
        one, two = 0, 0
        print(a)
        for n in a:
            three = max(n + one, two)
            one = two
            two = three
        print(two)
        return two