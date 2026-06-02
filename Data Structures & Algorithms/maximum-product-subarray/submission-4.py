class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        running_prod = 1
        max_prod, cur_prod = float('-inf'), 0
        sn = float('-inf')
        # [2, -1, 2, 0, 4, -5, -3]
        # i = 3
        # rp = -28
        # cur_prod = 14
        # sn = -2
        # max_prod = 2
        for num in nums:
            if num == 0:
                max_prod = max(0, max_prod)
                running_prod = 1
                sn = float('-inf')
                continue
            running_prod *= num
            if running_prod > 0:
                cur_prod = running_prod
            elif running_prod < 0:
                cur_prod = running_prod/sn if sn != float('-inf') else running_prod
                sn = max(sn, running_prod) # smallest negative value seen

            max_prod = max(max_prod, cur_prod)

        return int(max_prod)