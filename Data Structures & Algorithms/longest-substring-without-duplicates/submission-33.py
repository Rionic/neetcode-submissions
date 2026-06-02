class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque([])
        longest = 0
        l = 0
        # xxxx
        #   r
        #[x]
        for r in range(len(s)):
            if s[r] not in dq:
                dq.append(s[r])
                longest = max(len(dq), longest)
            else:
                dq.append(s[r])
                while dq[0] != s[r]:
                    dq.popleft()
                if dq:
                    dq.popleft()
        return longest
            