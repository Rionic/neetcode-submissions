class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        fleets = front_time = 0

        for p, s in cars:
            time = (target - p) / s
            if time > front_time:
                front_time = time
                fleets += 1

        
        return fleets