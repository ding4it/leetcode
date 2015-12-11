#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  PalindromeLinkedList.py
@time: 2015/12/25 11:08
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = head
        if head == None or head.next == None :
            return True
        p2 = p2.next
        if p2.next == None:
            return p1.val == p2.val
        if p2.next.next == None:
            return p1.val == p2.next.val

        prev = p1
        p1 = p1.next
        p2 = p2.next.next
        while p2.next != None and p2.next.next != None:
            tmp = p1
            p1 = p1.next
            tmp.next = prev
            prev = tmp
            p2 = p2.next.next

        if p2.next == None:
            p2 = p1.next
            p1.next = prev
        else:
            p2 = p1.next.next
            p1.next = prev
        while p2 != None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True