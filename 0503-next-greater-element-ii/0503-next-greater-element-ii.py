class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]
        res=[-1]*len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                res[stack.pop()]=nums[i]
            stack.append(i)
        for x in nums:
            while stack and x>nums[stack[-1]]:
                res[stack.pop()]=x
        return res