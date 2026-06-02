class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, combo):
            if sum(combo) == target and sorted(combo) not in res:
                res.append(sorted(combo[:]))
            if i == len(candidates):
                return
                
            combo.append(candidates[i])
            backtrack(i+1, combo)
            combo.pop()
            backtrack(i+1, combo)

        backtrack(0, [])
        return res