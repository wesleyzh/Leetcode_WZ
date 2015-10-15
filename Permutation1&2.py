class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, nums):
        if nums == []: return []
        
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution)+1):
                    next.append(solution[:i] + [num] + solution[i:])
            solutions = next
            
        return solutions
        
        

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    if solution[:i] + [num] + solution[i:] not in next:
                        next.append(solution[:i] + [num] + solution[i:])
            
            solutions = next
        return solutions