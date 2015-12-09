class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		import re
		p = re.compile('[a-zA-z]+')
		l = p.findall(s)
		l.reverse()
		l = " ".join(l)
		return l
s = Solution()
ans = s.reverseWords("the sky is blue")
print(ans)