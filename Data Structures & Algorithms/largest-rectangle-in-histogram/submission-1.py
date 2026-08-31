class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            while stack:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea