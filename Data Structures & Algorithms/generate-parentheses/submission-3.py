class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(r, l, subset):

            # Base case:
            if l + r == n*2:
                res.append(subset)
                return

            # Choose (
            if r < n:
                backtrack(r+1, l, subset + '(')

            # Choose )
            if l < n and l < r:
                backtrack(r, l+1, subset + ')')
            return res

        return backtrack(0, 0, '')