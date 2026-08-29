class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(reverse=True)

        times = []

        for c in cars:
            time = (target - c[0]) / c[1]

            if times and time <= times[-1]:
                continue
            else:
                times.append(time)

        return len(times)
        