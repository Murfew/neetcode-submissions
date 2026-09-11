class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / s
        fleets = 1

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        prevTime = (target - pairs[0][0]) / pairs[0][1]
        for p, s in pairs[1:]:
            time = (target - p) / s

            if time > prevTime:
                fleets += 1
                prevTime = time

        return fleets