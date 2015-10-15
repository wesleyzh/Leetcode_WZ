
"""
Let num = [1,2,3,...,n]. The first digit is k/(n-1)!, then let k = k % (n-1)! and remove this digit from num. The second digit is k/(n-2)!, then let k = k % (n-2)! and remove this digit from num and so on.
"""
import math
class Solution:
    def getPermutation(self, n, k):
        seq, k, fact = "", k -1, math.factorial(n - 1)
        perm = [i for i in range(1, n + 1)]
        for i in reversed(range(n)):
            curr = perm[k / fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq

A = 3
k = 1
solution = Solution()
print solution.getPermutation(A, k)