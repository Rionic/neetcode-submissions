import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Distance: [x, y], [x2, y2] ...
        distanceMap = defaultdict(list)
        for point in points:
            distanceMap[math.sqrt(point[0]**2 + point[1]**2)].append([point[0], point[1]])
        distances = list(distanceMap.keys())
        heapq.heapify(distances)
        
        res = []
        while k > 0:
            closest = heapq.heappop(distances)
            for xy in distanceMap[closest]:
                res.append(xy)
                k -= 1
                if k < 1:
                    break
        return res
        
            