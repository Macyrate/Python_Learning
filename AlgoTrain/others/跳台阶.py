# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a = 1
        b = 1
        i = 0
        while(i<number):
            a,b = b,a+b
            i += 1
        return a
		
jumper = Solution()
jumper.jumpFloor(10)