class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                water = max(water,(right-left) * height[left])
                left += 1
            else:
                water = max(water, (right-left) * height[right])
                right -= 1
        return water
