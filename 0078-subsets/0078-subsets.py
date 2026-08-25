class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def solve(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            solve(i+1)
            subset.pop()
            solve(i+1)
        solve(0)
        return res