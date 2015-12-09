class Solution:
	# @return a boolean
	def isScramble(self, s1, s2,tag = 0):
		if s1 == s2:
			return True
		set1 = set()
		set2 = set()
		set3 = set()
		length = len(s1)
		i = 0
		j = 0
		k = length -1
		while i < length-1:
			if tag == 0:
				set1.add(s1[i])
				set2.add(s2[j])
				set3.add(s2[k])
				i += 1
				j += 1
				k -= 1
				if set1 == set2:
					tmp = self.isScramble(s1[0:i],s2[0:j],2) and self.isScramble(s1[i:],s2[j:],0)
					if tmp:
						return True
				elif set1 == set3:
					tmp = self.isScramble(s1[0:i],s2[k+1:],1) and self.isScramble(s1[i:],s2[0:k+1],0)
					if tmp:
						return True
			elif tag == 1:
				set1.add(s1[i])
				set2.add(s2[j])
				i += 1
				j += 1
				if set1 == set2:
					tmp = self.isScramble(s1[0:i],s2[0:j],2) and self.isScramble(s1[i:],s2[j:],0)
					if tmp:
						return True
			elif tag == 2:
				set1.add(s1[i])
				set3.add(s2[k])
				i += 1
				k -= 1
				if set1 == set3:
					tmp = self.isScramble(s1[0:i],s2[k+1:],1) and self.isScramble(s1[i:],s2[0:k+1],0)
					if tmp:
						return True
		return False



s = Solution()
x = s.isScramble("pcighfdjnbwfkohtklrecxnooxyipj", "npodkfchrfpxliocgtnykhxwjbojie")
print(x)

		