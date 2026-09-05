class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        # water at i = min(maxLeftHeight, maxRightHeight) - height[i]
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])


        for i in range(len(height)):
            trapped = min(maxLeft[i], maxRight[i]) - height[i]
            water += trapped if trapped > 0 else 0

        return water