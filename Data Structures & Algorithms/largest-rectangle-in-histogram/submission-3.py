class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, start)
        largest = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                largest = max(largest, height * (i - index))
                start = index

            stack.append((h, start))

        while stack:
            height, index = stack.pop()
            largest = max(largest, height * (len(heights) - index))

        return largest