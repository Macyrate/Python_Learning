import time
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

    sel = int(input())
    start = time.time()         #计算运行时间
    if(sel == 1):
        import bubble_sort
        print(bubble_sort.bubble_sort(listin))
    elif(sel >=2 and sel<=6):
        print('开发中')
    else:
        raise ValueError('请输入正确的选项！')
    end = time.time()
    print('程序运行时间：%.2f us' % ((end - start)*1000))
    print('输入Q/q退出，或继续尝试其他算法')
    if input().lower() == 'q':
        exit(0)