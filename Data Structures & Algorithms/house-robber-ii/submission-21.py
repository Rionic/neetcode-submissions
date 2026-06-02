class Solution:
    def rob(self, nums: List[int]) -> int:
        def robSub(a):
            one, two = 0, 0
            print(a)
            for n in a:
                three = max(n + one, two)
                one = two
                two = three
            print(two)
            return two

        return max(robSub(nums[:-1]), robSub(nums[1:]), nums[0])

        