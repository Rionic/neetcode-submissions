class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [(-1, 0)] # why does L padding not fix?
        maxArea = 0
        heights.append(0)
        # [7,1,7,2,2,4]
        #    ^
        # s = [0 7]
        # max = 7
        for i, h in enumerate(heights):
            while len(s) > 1 and s[-1][1] > h:
                l, cur_h = s.pop()
                if s:
                    l = s[-1][0] + 1

                maxArea = max(maxArea, cur_h * (i - l))
        
            # maxArea = max(maxArea, h)
            s.append((i, h))
        heights.pop()
        return max(maxArea, len(heights) * min(heights))