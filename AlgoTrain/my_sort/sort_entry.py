print('请输入要进行排序的序列')
listin = list(map(float,input().split()))
print(listin)

print('''
用什么算法进行排序？
1.冒泡排序  2.快速排序
3.插入排序  4.选择排序
5.堆排序    6.归并排序
''')

sel = int(input())
if(sel == 1):
    import bubble_sort
    print(bubble_sort.bubble_sort(listin))
elif(sel >=2 and sel<=6):
    print('开发中\n')
else:
    print('请输入正确的选项\n')