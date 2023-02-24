def numDistinct(s: str, t: str) -> int:
    dp = {}

    def dfs(idxS, idxT):
        if idxS == len(s):
            return 0

        if idxT == len(t):
            return 1

        if (idxS, idxT) in dp:
            return dp[(idxS, idxT)]

        # ways=0
        if s[idxS] == t[idxT]:
            dp[(idxS, idxT)] = dfs(idxS+1, idxT+1)+dfs(idxS+1, idxT)

        else:
            dp[(idxS, idxT)] = dfs(idxS+1, idxT)
        return dp[(idxS, idxT)]
    return dfs(0, 0)


s = "rabbbit"
t = "rabbit"
numDistinct(s, t)
