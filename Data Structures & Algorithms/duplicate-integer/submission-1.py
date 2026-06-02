class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = []
        for num in nums:
            if num in dupes:
                return True
            dupes.append(num)
        return False