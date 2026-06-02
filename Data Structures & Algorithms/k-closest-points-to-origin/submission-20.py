import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append([distance, point[0], point[1]])
        heapq.heapify(distances)
        
        res = []
        while k > 0:
            res.append(heapq.heappop(distances)[1:])
            k -= 1
        return res
        
            