class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1
        lo=0
        hi=len(nums)-1
        while hi>=lo:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            if nums[lo]<=nums[mid]:
                if nums[mid]>target>=nums[lo]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[hi]>=target>nums[mid]:
                    lo=mid+1
                else:
                    hi=mid-1
        return -1