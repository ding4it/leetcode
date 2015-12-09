class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
    	if n == 0:
    		return 1
    	elif n < 0:
    		return 1/self.pow(x, -n)
    	else:
    		rs = 1
    		t = x
    		while n > 0:
    			if n %2 == 1:
    				rs *= t
    			t *= t
    			n = n//2
    		return rs


s = Solution()
k = s.pow(2,10)
print(k)