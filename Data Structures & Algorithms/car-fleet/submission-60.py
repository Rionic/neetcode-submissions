class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 2: return len(position)

        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        fleets = 0
        front_time = 0

        for p, s in cars:
            time = (target - p) / s
            # fleet is formed if this car is slower than carfleet ahead
            if time > front_time:
                front_time = time
                fleets += 1

        
        return fleets