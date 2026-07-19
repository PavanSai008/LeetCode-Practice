class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # m=max(arr)+k
        # c=0
        # for x in range(1,m+1):
        #     if x in arr:
        #         continue
        #     c+=1
        #     if c==k:
        #         return x
        l,r=0,len(arr)
        while l<r:
            m=(l+r)//2
            miss=arr[m]-m-1
            if miss<k:
                l=m+1
            else:
                r=m
        return l+k
            