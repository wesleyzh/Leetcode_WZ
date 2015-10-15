class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if S == []: return []
        
        def dfs(deep, start, valuelist):
            if valuelist not in res: res.append(valuelist)
            if deep == len(S): return
            for i in range(start, len(S)):
                dfs(deep+1, i+1, valuelist + [S[i]])
                
        S.sort()
        res = []
        dfs(0,0,[])
        
        return res