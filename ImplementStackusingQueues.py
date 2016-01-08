#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  ImplementStackusingQueues.py
@time: 2016/1/8 10:53
"""
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__queue__ = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp = []
        tmp.append(x)
        while self.__queue__:
            tmp.append(self.__queue__[0])
            del self.__queue__[0]
        self.__queue__ = tmp
        print(self.__queue__)



    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return
        del self.__queue__[0]




    def top(self):
        """
        :rtype: int
        """
        return self.__queue__[0]



    def empty(self):
        """
        :rtype: bool
        """
        if not self.__queue__:
            return True
        else:
            return False


A = Stack()
A.push(1)
A.empty()
