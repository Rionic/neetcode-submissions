class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 0
        numset = set(nums)
        i = 0
        cur = next(iter(numset))
        b = 0
        while numset and b < 5:
            b += 1
            print(numset, cur)
            if cur - 1 not in numset:
                cur_len = 1
                longest = max(cur_len, longest)
                numset.remove(cur)
                cur += 1
                while cur in numset:
                    print(cur)
                    numset.remove(cur)
                    cur_len += 1
                    cur += 1
                    longest = max(cur_len, longest)
                if not numset: break
                cur = next(iter(numset))
            else: 
                cur -= 1

        return longest

