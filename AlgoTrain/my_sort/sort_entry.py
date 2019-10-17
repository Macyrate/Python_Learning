import time

import bubble_sort
import quick_sort
import insertion_sort
import selection_sort
import heap_sort
import merge_sort

print('请输入要进行排序的序列')
listin = list(map(float,input().split()))
print(listin)

try:
    while(1):
        print('''
        用什么算法进行排序？
        1.冒泡排序  2.快速排序
        3.插入排序  4.选择排序
        5.堆排序    6.归并排序
        ''')

        sel = input()
        start = time.time()         #计算运行时间
        if(sel == '1'):
            print(bubble_sort.bubble_sort(listin))
        elif(sel == '2'):
            deallist = listin[:]
            quick_sort.quick_sort(deallist, 0, len(deallist)-1)
            print(deallist)
        elif(sel == '3'):
            print(insertion_sort.insertion_sort(listin))
        elif(sel == '4'):
            print(selection_sort.selection_sort(listin))
        elif(sel == '5'):
            print(heap_sort.heap_sort(listin))
        elif(sel == '6'):
            deallist = listin[:]
            print(merge_sort.merge_sort(deallist))
        else:
            raise ValueError
        end = time.time()
        print('程序运行时间：%f ns' % ((end - start)*1000000))
        print('输入Q/q退出，或继续尝试其他算法')
        if input().lower() == 'q':
            exit(0)
except ValueError:
    print('请输入正确的值！')