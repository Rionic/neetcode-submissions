class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        segment = [0] * (len(s)+1)
        segment[0] = 1

        for i in range(1, len(s)+1):
            for word in wordDict:
                if len(word) <= i and s[i - len(word):i] == word and segment[i - len(word)]:
                    segment[i] = 1
                    break
        return segment[-1] == 1