class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque([])
        longest = 0
        l = 0
        # xxxx
        #   r
        #[x]
        for c in s:
            if c not in dq:
                dq.append(c)
                longest = max(len(dq), longest)
            else:
                dq.append(c)
                while dq[0] != c:
                    dq.popleft()
                if dq:
                    dq.popleft()
        return longest
            