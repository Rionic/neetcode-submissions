class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        s = [(0, -1)]
        heights.append(0)

        for i, h in enumerate(heights):
            while len(s) > 1 and h < s[-1][0]:
                c, _ = s.pop()
                maxArea = max(maxArea, c*(i-1 - s[-1][1]))
            s.append((h, i))
        
        return maxArea






