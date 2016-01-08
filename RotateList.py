#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  RotateList.py
@time: 2016/1/7 20:27
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        i = 1
        tmp = head
        while tmp.next:
            i +=1
            tmp = tmp.next
        tmp.next = head
        i = i-k%i
        while i>0:
            tmp = tmp.next
            i -= 1
        rs = tmp.next
        tmp.next = None
        return rs
