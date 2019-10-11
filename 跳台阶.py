# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a = 1
        b = 1
        for i in range(number):
            a,b = b,a+b
        return a
		
jumper = Solution()
jumper.jumpFloor(10)