class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] > heights[r]:
                water = max(water, heights[r] * (r - l))
                r -= 1
            else:
                water = max(water, heights[l] * (r - l))            
                l += 1

        return water