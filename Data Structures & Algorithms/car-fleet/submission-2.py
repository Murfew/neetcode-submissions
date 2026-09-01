class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        fleets = []

        for p, s in sorted(pairs, reverse=True):
            time = (target - p) / s

            if fleets and fleets[-1] >= time:
                continue

            fleets.append(time)


        return len(fleets)
