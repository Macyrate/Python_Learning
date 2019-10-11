# 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
# 针对所有的元素重复以上的步骤，除了最后一个；
# 重复步骤1~3，直到排序完成。
def bubble_sort(listin):
    deallist = listin[:]
    for x in range(0,len(deallist)):
        for y in range(0,len(deallist)-1-x):
            if deallist[y] > deallist[y+1]:
                deallist[y],deallist[y+1] = deallist[y+1],deallist[y]
    return deallist