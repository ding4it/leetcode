class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num % 2 == 0:
            num = num//2
        while num % 3 == 0:
            num = num//3
        while num % 5 == 0:
            num = num//5
        return num != 1


    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = list([1])
        x2 = 0
        x3 = 0
        x5 = 0
        while len(a) <n:
            t2 = a[x2]*2
            t3 = a[x3]*3
            t5 = a[x5]*5
            t = min(t2,t3,t5)
            a.append(t)
            if t == t2:
                x2 += 1
            if t == t3:
                x3 += 1
            if t == t5:
                x5 += 1
        return a[n-1]

