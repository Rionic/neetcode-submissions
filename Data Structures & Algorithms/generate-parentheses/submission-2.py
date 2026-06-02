class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(subset):
            s = []
            for b in subset:
                if b == '(':
                    s.append(b)
                else:
                    if len(s) == 0:
                        return False
                    s.pop()
            return True

        def backtrack(r, l, subset):

            # Base case:
            if l == 0 and r == 0:
                if valid(subset):
                    res.append(subset)
                return

            # Choose (
            if r != 0:
                backtrack(r-1, l, subset + '(')

            # Choose )
            if l != 0:
                backtrack(r, l-1, subset + ')')
            return res

        return backtrack(n, n, '')