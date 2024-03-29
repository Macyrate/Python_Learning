# 从第一个元素开始，该元素可以认为已经被排序；
# 取出下一个元素，在已经排序的元素序列中从后向前扫描；
# 如果该元素（已排序）大于新元素，将该元素移到下一位置；
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
# 将新元素插入到该位置后；
# 重复步骤2~5。

def insertion_sort(listin):
    deallist = listin[:]
    if len(deallist) <= 1:
        return deallist
    for x in range(1,len(deallist)):
        target = deallist[x]
        t = x
        while t > 0 and target < deallist[t-1]:
            deallist[t] = deallist[t-1]
            t -= 1
        deallist[t] = target
    return deallist