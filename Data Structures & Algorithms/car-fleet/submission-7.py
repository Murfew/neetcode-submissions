class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        pairs = [(p, s) for p, s in zip(position, speed)]

        for p, s in sorted(pairs, reverse=True):
            time = (target - p) / s

            if fleets and time <= fleets[-1]:
                continue
            else:
                fleets.append(time)

        return len(fleets)