# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		l = []
		i = 1
		start = head
		while i < m:
			head = head.next
			i = i+i
		start = head
		while i < n + 1:
			val = head.val
			l.append(val)
			i = i+1
			head = head.next
		while len(l) > 0:
			start.val = l.pop()
			start = start.next
		return head