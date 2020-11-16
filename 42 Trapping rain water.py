class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        j = 0
        k = len(height) - 1
        left_max = 0
        right_max = 0
        while j < k:
            if height[j] < height[k]:
                if height[j] >= left_max:
                    left_max = height[j]
                else:
                    ans += left_max - height[j]
                j += 1
            else:
                if height[k] >= right_max:
                    right_max = height[k]
                else:
                    ans += right_max - height[k]
                k -= 1
        return ans
