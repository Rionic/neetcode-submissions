class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            
            # If the tank drops below 0, we can't start from any station up to i
            if total < 0:
                start = i + 1
                total = 0
                
        return start