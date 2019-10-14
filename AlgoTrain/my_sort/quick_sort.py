# 从数列中挑出一个元素，称为 “基准”（pivot）；
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

def quick_sort(listin, left, right):
    if left < right:
        pivotkey = partition(listin, left, right)
        quick_sort(listin, left, pivotkey - 1)
        quick_sort(listin, pivotkey, right)

def partition(listin,left,right):
    pivotvalue = listin[right]
    lastlesskey = left - 1
    for x in range(left,right):                                         #扫描除最右的pivot以外的元素
        if listin[x] <= pivotvalue:
            lastlesskey += 1
            listin[lastlesskey], listin[x] = listin[x], listin[lastlesskey]                 #对不大于pivot值的元素，换到“小”区的最后；否则不动，作为“大”区
    listin[lastlesskey + 1], listin[right] = listin[right], listin[lastlesskey + 1]         #由于基准在最后，将基准pivot与“大”区的第一个元素互换位置，即放到了中间（i+1的位置）
    return lastlesskey + 1
