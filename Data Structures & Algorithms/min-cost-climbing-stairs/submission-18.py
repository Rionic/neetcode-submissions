class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0: return 0
        if len(cost) == 1: return cost[0]
        totalCost = [0] * len(cost)
        totalCost[-1] = cost[-1]
        totalCost[-2] = cost[-2]
        for i in range(len(cost) - 3, -1, -1):
            print(totalCost[i], min(totalCost[i+1], totalCost[i+2]))
            totalCost[i] = cost[i] + min(totalCost[i + 1], totalCost[i + 2])
        print(totalCost)
        return min(totalCost[0], totalCost[1])
