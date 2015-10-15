class Solution:
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:  #find the largest one keep incresment 
                k = i
        if k == -1:                  #list is sorted with decent order
            return num[::-1]         #reverse
        for i in range(len(num)):
            if num[i] > num[k]:
                l = i
        num[k], num[l] = num[l], num[k]
        print num[:k + 1]   #from 0 to k
        print num[:k: -1]   #reverse from k to en
        return num[:k + 1] + num[:k:-1]
    

A = [1,3,2]
solution = Solution()
print solution.nextPermutation(A)
