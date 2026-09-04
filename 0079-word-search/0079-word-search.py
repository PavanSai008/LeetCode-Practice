class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def complete(i,j,x):
            if x==len(word):
                return True
            if 0>i or i>=len(board) or 0>j or j>=len(board[0]):
                return False
            if board[i][j]!=word[x]:
                return False
            temp=board[i][j]
            board[i][j]="X"
            found=(
                complete(i+1,j,x+1) or
                complete(i,j+1,x+1) or
                complete(i-1,j,x+1) or
                complete(i,j-1,x+1)
            )
            board[i][j]=temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if complete(i,j,0):
                        return True
        return False

