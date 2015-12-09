# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
    	rs = []
    	stack = []
    	now = root
        stack.append([now,0])
        while len(stack) != 0:
        	now,time = stack.pop()
        	if now == None:
        		continue
        	if time == 0:
        		stack.append([now,1])
        		stack.append([now.left,0])
        	elif time == 1:
        		stack.append([now,2])
        		stack.append([now.right,0])
        	else:
        		rs.append(now.val) 
        return rs