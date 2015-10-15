# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None: return []
         
        solution = []
        thisLevel =[]
        if root != None:
            thisLevel.append(root)
        leftToRight = True
        while len(thisLevel)>0:
            levelSolution = []
            nextLevel = []
            while len(thisLevel)>0:
                node = thisLevel.pop()
                levelSolution.append(node.val)
                if leftToRight:
                    if node.left != None:
                        nextLevel.append(node.left)
                    if node.right != None:
                        nextLevel.append(node.right)
                else:
                    if node.right != None:
                        nextLevel.append(node.right)
                    if node.left != None:
                        nextLevel.append(node.left)
            thisLevel = nextLevel
            solution.append(levelSolution)
            leftToRight = not leftToRight
        return solution