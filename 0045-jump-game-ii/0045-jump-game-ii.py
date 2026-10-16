class Solution:
    def jump(self, nums: List[int]) -> int:
        j=e=f=0
        for i in range(len(nums)-1):
            f=max(f,i+nums[i])
            if i==e:
                e=f
                j+=1
        return j
