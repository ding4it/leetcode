class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        tmp = set()
        rs = set()
        for i in range(l - 9):
        	if s[i:i+10] in tmp:
        		rs.add(s[i:i+10])
        	else:
        		tmp.add(s[i:i+10])
        return list(rs)