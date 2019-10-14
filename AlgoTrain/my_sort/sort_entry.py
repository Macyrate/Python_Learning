import time

import bubble_sort
import quick_sort
import insertion_sort

print('请输入要进行排序的序列')
listin = list(map(float,input().split()))
print(listin)

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
    if(sel == '2'):
        deallist = listin[:]
        quick_sort.quick_sort(deallist, 0, len(deallist)-1)
        print(deallist)
    if(sel == '3'):
        print(insertion_sort.insertion_sort(listin))
    # elif(sel >=3 and sel<=6):
    #     print('开发中')
    # else:
    #     raise ValueError('请输入正确的选项！')
    end = time.time()
    print('程序运行时间：%f ns' % ((end - start)*1000000))
    print('输入Q/q退出，或继续尝试其他算法')
    if input().lower() == 'q':
        exit(0)
