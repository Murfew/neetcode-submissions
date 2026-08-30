class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort the cars (pos, speed) in desc order
        # Traverse the cars and see if that car catches up to the fleet in front of it
        # If it does, it joins the fleet
        # If not, it create a new fleet with a new arrival time

        pairs = [(p, s) for p, s in zip(position, speed)]
        fleets = []

        for p, s in sorted(pairs, reverse=True):
            arrivalTime = (target - p) / s

            if fleets and arrivalTime <= fleets[-1]:
                continue
            
            fleets.append(arrivalTime)

        return len(fleets)