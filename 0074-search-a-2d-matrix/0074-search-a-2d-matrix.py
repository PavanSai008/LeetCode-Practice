class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=(m*n)-1
        while l<=r:
            mid=(l+r)//2
            i=mid//n
            j=mid%n
            if target==matrix[i][j]:
                return True
            elif target<matrix[i][j]:
                r=mid-1
            else :
                l=mid+1
        return False