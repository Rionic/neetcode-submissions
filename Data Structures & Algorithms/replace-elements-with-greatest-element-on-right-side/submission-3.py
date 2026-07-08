class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = 0

        a2 = [-1] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            m = max(m, arr[i+1])
            a2[i] = m
        return a2