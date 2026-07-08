class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        # for i, n in enumerate(nums):
        #     ans.append(nu)
        ans.extend(ans)
        return ans