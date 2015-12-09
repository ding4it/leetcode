class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) ==0 :
            return False
        if len(nums) <= k:
            return len(nums) != len(set(nums))
        return any([len(nums[i:i+k+1]) != len(set(nums[i:i+k+1])) for i in range(len(nums)-k)])

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) <=1 or k == 0:
            return False
        if len(nums) <= k:
            x = sorted(nums)
            return any(map(lambda x,y:abs(x-y)<=t,x[0:-1],x[1:]))
        for i in range(0,len(nums)-k):
            x = sorted(nums[i:i+k+1])
            if any(map(lambda x,y:abs(x-y)<=t,x[0:-1],x[1:])):
                return True
        return False


x = Solution()
t = x.containsNearbyAlmostDuplicate([1,2,1], 1, 1)
print(t)