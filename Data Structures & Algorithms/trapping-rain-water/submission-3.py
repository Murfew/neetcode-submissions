class Solution:
    def trap(self, height: List[int]) -> int:
        # water[i] = min(height[maxLeft], height[maxRight]) * (maxRight - maxLeft)

        total = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                water = maxLeft - height[l]
                total += water if water > 0 else 0
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                water = maxRight - height[r]
                total += water if water > 0 else 0
                maxRight = max(maxRight, height[r])
                r -= 1


        return total