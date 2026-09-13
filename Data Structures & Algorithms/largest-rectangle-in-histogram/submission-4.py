class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, start)
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                res = max(res, height * (i - index))
                start = index

            stack.append([h, start])

        while stack:
            height, index = stack.pop()
            res = max(res, height * (len(heights) - index))

        return res