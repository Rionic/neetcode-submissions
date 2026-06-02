class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 0
        numset = set(nums)
        cur = next(iter(numset))
        while numset:
            cur_len = 0
            if cur - 1 not in numset: # Begin sequence
                # cur_len = 1
                # longest = max(cur_len, longest)
                # numset.remove(cur)
                # cur += 1
                while cur in numset:
                    numset.remove(cur)
                    cur_len += 1
                    cur += 1
                    longest = max(cur_len, longest)
                if not numset: break
                cur = next(iter(numset))
            else: 
                cur -= 1

        return longest

