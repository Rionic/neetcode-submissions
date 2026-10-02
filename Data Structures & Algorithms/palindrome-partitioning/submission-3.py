class Solution:
    def partition(self, s: str) -> List[List[str]]:
       
        palindromes = []

        def backtrack(path, start):
            if start == len(s):
                palindromes.append(path[:])

            for end in range(start + 1, len(s) + 1):
                piece = s[start: end]
                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(path, end)
                    path.pop()


        backtrack([], 0)

        return palindromes
        
        