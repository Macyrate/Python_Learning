# 把长度为n的输入序列分成两个长度为n/2的子序列；
# 对这两个子序列分别采用归并排序；
# 将两个排序好的子序列合并成一个最终的排序序列。
# 我这个实现没有包含拷贝原序列的部分，进行的是原地排序

def merge_sort(listin):
    n = len(listin)
    if n <= 1:          # 两种基本情况
        return listin
    elif n == 2:
        if listin[0] > listin[1]:
            listin[0],listin[1] = listin[1],listin[0]
        return listin

    else:
        mid = n//2
        front = merge_sort(listin[:mid])        # 递归调用归并排序
        back = merge_sort(listin[mid:n])
        i,j = 0,0
        while i < len(front) and j < len(back):         # 合并两个已排序的序列
            if front[i] <= back[j]:
                listin[i+j] = front[i]
                i += 1
            else:
                listin[i+j] = back[j]
                j += 1
        listin = listin[:i+j]
        listin.extend(front[i:])        #注意extend直接对原list操作，返回值是NoneType，不要用来赋值
        listin.extend(back[j:])
        return listin