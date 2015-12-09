__author__ = 'DWJ'

class Solution:
    def reOrderArray(self, array):
        # write code here
         return sorted(array, key=lambda x: x%2,reverse=True )
x = Solution()

t = x.reOrderArray([1,2,3,4,5,6,7])
print("ferawf")
print(t)