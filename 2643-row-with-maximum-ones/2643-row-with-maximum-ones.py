class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = []
        for x in range(len(mat)):
            cnt = 0
            for i in mat[x]:
                if i == 1:
                    cnt += 1
            ans.append((cnt, x))
        c, res = max(ans)
        sol = []
        for i, x in ans:
            if i == c:
                sol.append((x, i))
        return sol[0]
