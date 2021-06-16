def minInsertions(s):
    memo = {}
    def dfs(s):
       
        if not s or s == s[::-1]:
            return 0
        if s in memo:
            return memo[s]
        if s[0] == s[-1]:
            memo[s] = dfs(s[1:-1])
        else:
            memo[s] = 1 + min(dfs(s[1:]), dfs(s[:-1]))
        return memo[s]
    return dfs(s)
print(minInsertions("mbadm"))
print(minInsertions("zzazz"))