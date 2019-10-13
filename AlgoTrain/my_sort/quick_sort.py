# 从数列中挑出一个元素，称为 “基准”（pivot）；
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

def quick_sort(listin, left, right):
    if left < right:
        pivot = partition(listin, left, right)
        quick_sort(listin, left, pivot - 1)
        quick_sort(listin, pivot, right)

def partition(listin,left,right):
    x = listin[right]
    i = left - 1
    for j in range(left,right):
        if listin[j] <= x:
            i += 1
            listin[i], listin[j] = listin[j], listin[i]
    listin[i + 1], listin[right] = listin[right], listin[i + 1]
    return i + 1







