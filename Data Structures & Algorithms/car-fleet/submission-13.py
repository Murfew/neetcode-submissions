class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_speed = list(zip(position, speed))
        pos_and_speed.sort(reverse=True)

        fleets = 1
        bottleneck = (target - pos_and_speed[0][0]) / pos_and_speed[0][1]

        for pos, speed in pos_and_speed[1:]:
            time_to_target = (target - pos) / speed
            if time_to_target > bottleneck:
                bottleneck = time_to_target
                fleets += 1

        return fleets