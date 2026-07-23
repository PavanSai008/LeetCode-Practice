class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        def find_max_row(col):
            ele,row=-1,-1
            for i in range(n):
                if mat[i][col]>ele:
                    ele=mat[i][col]
                    row=i
            return row
        l,r=0,m-1
        while l<=r:
            mid=(l+r)//2
            row=find_max_row(mid)
            left=mat[row][mid-1] if mid-1>=0 else -1
            right=mat[row][mid+1] if mid+1<m else -1
            if left<mat[row][mid] and mat[row][mid]>right:
                return [row,mid]
            elif right>mat[row][mid]:
                l=mid+1
            else:
                r=mid-1
