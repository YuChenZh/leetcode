# 39 Combination Sum
'''
Given an array of distinct integers candidates and a target integer target, return a 
list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.The same number may be chosen from candidates 
an unlimited number of times. Two combinations are unique if the frequency of at least one 
of the chosen numbers is different.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resu = []
        self.backtracking(candidates,target,[],resu)
        return resu
    
    def backtracking(self,nums,target,subset,resu):
        if target < 0:
            return
        if target == 0:
            resu.append(subset)
        for i in range(len(nums)):
            self.backtracking(nums[i:],target-nums[i],subset+[nums[i]],resu)

# 40 Combination Sum II
'''
Given a collection of candidate numbers (candidates) and a target number (target), find 
all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:       
        res = []
        self.backtracking(res,0,[],sorted(candidates),target)
        return res       
    
    def backtracking(self,res,idx,subset,nums,target):
        if target < 0:
            return
        if target == 0:
            res.append(subset)
        for i in range(idx,len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.backtracking(res,i+1,subset+[nums[i]],nums,target-nums[i])

# 46. Permutations
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:           
    res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
                
# 47. Permutations II 
'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
# 78. Subsets
'''
Given an integer array nums, return all possible subsets (the power set).
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
		# DFS
        self.res = []
        self.dfs(nums, 0, [])
        return self.res
    
    def dfs(self, nums, pos, tmp):
        self.res.append(tmp)
        for i in range(pos, len(nums)):
            self.dfs(nums, i+1, tmp+[nums[i]])
            
# 90. Subsets II  
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:                  
  # solution 1: not space efficient           
        resu = set()
        # sort nums first to avoid duplicate subsets, e,g,.[1,2] and [2,1]
        self.backtracking(resu,sorted(nums),[],0)
        return list(resu)
    
    def backtracking(self,resu,nums,subset,idx):
        # list is unhashble, convert subset to tuple then add to resu
        resu.add(tuple(subset))  
        for i in range(idx,len(nums)):
            self.backtracking(resu,nums,subset+[nums[i]],i+1)
