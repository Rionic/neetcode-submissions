class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.extend([0, 0])

        one, two = cost[-1], cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            three = min(one, two) + cost[i]
            one = two
            two = three
        return min(one, two)
