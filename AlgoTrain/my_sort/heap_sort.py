# 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
# 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
# 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。


def heap_sort(listin):
    def heap_adjust(arr,start,end):
        #将以start为根节点的堆调整为大根堆
        #这个函数并不能直接完全调整，必须自底向上逐个进行调用才行
        temp = arr[start]
        son = 2*start + 1           #完全二叉树的性质，左子节点
        while son <= end:
            if son < end and arr[son] < arr[son+1]:   
                son += 1        #找出左右子节点中较大的  
            if temp >= arr[son]:
                break
            arr[start] = arr[son]      #子节点上移
            start = son
            son = 2*start +1
        arr[start] = temp       #原堆顶插入到正确位置

    deallist = listin[:]
    n = len(deallist)
    if n <= 1:
        return deallist
    root = n//2-1   #完全二叉树性质，最后一个非叶结点
    for i in range(root,-1,-1):        #对堆的非叶节点自底向上逐个调用
        heap_adjust(deallist,i,n-1)
    #至此，已将序列构建为大顶堆。

    n -= 1      #准备掐掉堆顶
    while n>=0:
        deallist[0],deallist[n] = deallist[n],deallist[0]
        heap_adjust(deallist,0,n-1)         #调整剩余部分为大根堆（这次无需遍历）
        n -= 1
    return deallist



    
    
    
