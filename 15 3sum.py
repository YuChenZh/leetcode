def threeSum(self, nums: List[int]) -> List[List[int]]:
        resu = []
        nums.sort()
        if len(nums) < 3:
            resu = []
        else:
            if set(nums) == {0}:
                resu.append(nums[0:3])
            else:
                for i in range(len(nums)):
                    if nums[i] == nums[i-1]:
                        continue
                    target = -nums[i]
                    j,k = i+1, len(nums)-1
                    while j < k:
                        if nums[j] + nums[k] == target:
                            resu.append([nums[i],nums[j],nums[k]])
                            j += 1
                            while j < k and nums[j] == nums[j-1]:
                                j += 1
                        elif nums[j] + nums[k] < target:
                            j += 1
                        else:
                            k -= 1
        return resu
