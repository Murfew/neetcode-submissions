class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        fleets = 0

        prevTime = 0
        for p, s in pairs:
            time = (target - p) / s

            if time > prevTime:
                fleets += 1
                prevTime = time
            

        return fleets