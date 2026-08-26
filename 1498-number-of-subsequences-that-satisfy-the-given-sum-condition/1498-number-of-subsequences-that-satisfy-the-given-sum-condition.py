class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # self.res=0
        nums.sort()
        # def solve(i,summ):

        #     if i==len(nums):
        #         if summ and summ[-1]+summ[0]<=target:
        #             self.res+=1
        #         return
        #     summ.append(nums[i])
        #     solve(i+1,summ)
        #     summ.pop()
        #     solve(i+1,summ)
        # solve(0,[])
        # return self.res
        l=0
        r=len(nums)-1
        res=0
        while l<=r:
            if nums[l]+nums[r]<=target:
                res+=2**(r-l)
                l+=1
            else:
                r-=1
        return res%(10**9+7)