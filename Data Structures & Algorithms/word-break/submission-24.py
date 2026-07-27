class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def checkWord(word, i):
            if len(word) > i:
                return False
            if s[i - len(word):i] == word:
                return True
            else: return False

        segment = [0] * (len(s)+1)
        segment[0] = 1

        for i in range(1, len(s)+1):
            for word in wordDict:
                if checkWord(word, i):
                    print('success', i)
                    if segment[i - len(word)]:
                        print('w')
                        segment[i] = 1
                        break
        print(segment)
        return segment[-1] == 1