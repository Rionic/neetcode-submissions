class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque([])
        longest = 0
        for c in s:
            if c not in dq:
                dq.append(c)
                longest = max(len(dq), longest)
            else:
                dq.append(c)
                l = dq.popleft()
                while l != c:
                    l = dq.popleft()

        return longest
            