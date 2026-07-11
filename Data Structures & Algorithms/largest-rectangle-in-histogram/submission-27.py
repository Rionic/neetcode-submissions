class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [(-1, 0)] 
        maxArea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while len(s) > 1 and s[-1][1] > h:
                l, cur_h = s.pop()
                maxArea = max(maxArea, cur_h * (i - 1 - s[-1][0]))
            s.append((i, h))

        return maxArea