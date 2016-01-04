#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  BinaryTreeInorderTraversal.py
@time: 2016/1/2 18:45
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        tmp = root
        rs = []
        while tmp != None:
            lst.append(tmp)
            tmp = tmp.left
        while len(lst) > 0:
            top = lst.pop()
            rs.append(top.val)
            if top.right != None:
                tmp = top.right
                while tmp != None:
                    lst.append(tmp)
                    tmp = tmp.left
        return rs


