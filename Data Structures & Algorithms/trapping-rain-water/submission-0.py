class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        prefix = [0] * n
        suffix = [0] * n

        for i in range(1, n):
            prefix[i] = max(height[i - 1], prefix[i - 1])
            
        for i in range(n - 2, -1, -1):
            suffix[i] = max(height[i + 1], suffix[i + 1])

        for i in range(n):
            water = min(prefix[i], suffix[i]) - height[i]
            total += water if water >= 0 else 0

        return total