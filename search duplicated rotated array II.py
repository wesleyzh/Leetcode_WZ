class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        return self.searchRecur(A, target, len(A) - 1, 0)
            
    def searchRecur(self, A, target, high, low):
        if high < low:
            return False
        mid = (high + low) / 2
        if A[mid] == target:
            return True
        while A[low] == A[mid] and A[mid] == A[high] and high > low:
            low, high = low + 1, high - 1
        if (A[0] <= A[mid] and target < A[mid] and target >= A[0]) or (A[mid] <= A[high] and (target < A[mid] or target > A[high])):
            return self.searchRecur(A, target, mid - 1, low)
        else:
            return self.searchRecur(A, target, high, low + 1)
        
        
a = [3,1,1,1]
target = 3

solution = Solution()
print solution.search(a,target)