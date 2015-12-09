class Solution:
    # @return a string
    def getPermutation(self, n, k):
    	return self.step(n,k,list(range(1,n+1)))
 
    def step(self,n,k,arr):
    	if n == 1:
    		return str(arr[0])
    	if k == 0:
    		return "".join(str(i) for i in arr)
    	f = self.factorial(n-1)
    	x = k % f if k % f else f
    	y = (k + f - 1) // f - 1
    	tmp = arr[y]
    	arr.remove(tmp)
    	return str(tmp) + self.step(n-1,x,arr)

    def factorial(self,n):
    	if n == 1 :
    		return 1
    	return n*self.factorial(n-1)


    	
s = Solution()
x = s.getPermutation(9,2)
print(x)	       
        