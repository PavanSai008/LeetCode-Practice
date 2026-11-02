class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        # left=[0]*(n+1)
        # right=[0]*(n+1)
        # left[0]=1
        # right[n-1]=1
        # summ=0
        # for i in range(1,n):
        #     if ratings[i]>ratings[i-1]:
        #         left[i]=left[i-1]+1
        #     else:
        #         left[i]=1
        # for i in range(n-2,-1,-1):
        #     if ratings[i]>ratings[i+1]:
        #         right[i]=right[i+1]+1
        #     else:
        #         right[i]=1 
        # for i in range(n+1):
        #     summ+=max(left[i],right[i])
        # return summ
        candy=[1]*n
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                candy[i]=candy[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)
        return sum(candy)