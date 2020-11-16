class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        resu = 0
        minvalue = float('inf')
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = abs(target - s)
                if diff == 0:
                    return s
                if diff < minvalue:
                    minvalue = diff
                    resu = s
                if s < target:
                    j += 1
                else:
                    k -= 1
        return resu
