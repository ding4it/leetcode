#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Ding4it
@license: Apache Licence 
@contact: ding4it@gmail.com
@file:  GameofLife.py
@time: 2016/1/11 21:49
"""

class Solution(object):
    def generate(self,board,x,y,n,m):
        rs = - (board[x][y] & 1)
        for i in range( max(x-1,0), min(x+2,n) ):
            for j in range( max(y-1,0),min(y+2,m) ):
                rs += board[i][j]&1
        return rs

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n==0:
            return
        m = len(board[0])
        if n == 1:
            for i in range(m):
                board[0][i] = 0
            return
        if m == 1:
            for i in range(n):
                board[i][0] = 0
            return
        for i in range(n):
            for j in range(m):
                alive = self.generate(board,i,j,n,m)
                if board[i][j] == 1 and 1 < alive< 4 :
                    board[i][j] = 3
                elif alive == 3:
                    board[i][j] = board[i][j] | 2

        print(board)
        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1
        print(board)

        return

a = Solution()
a.gameOfLife([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]])