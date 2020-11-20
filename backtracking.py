# 39 Combination Sum
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
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:           
    
    # Level0: []
    # level1: [1]                  [2]              [3]
    # level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    # level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1] 
    
    ## redo
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res       
    
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
                
# 47. Permutations II 
class Solution:
    # need to improve, not time efficient
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res       
    
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            if subset not in res:
                res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
