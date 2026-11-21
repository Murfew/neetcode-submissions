class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (temp, day)

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_day = stack.pop()
                result[stack_day] = day - stack_day
            stack.append((temp, day))

        return result