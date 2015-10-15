class Solution:
    def uniquePaths(self, m, n):
        N = m - 1 + n - 1
        K = min(m, n) - 1
        # calculate C(N, K)
        res = 1
        for i in xrange(K):
            res = res * (N - i) / (i + 1)
        return res
    

m = 3
n = 7

solution = Solution()
print solution.uniquePaths(m,n)