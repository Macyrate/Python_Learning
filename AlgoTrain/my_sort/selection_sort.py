# 初始状态：无序区为R[1..n]，有序区为空；
# 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
# n-1趟结束，数组有序化了。

def selection_sort(listin):
    deallist = listin[:]
    for x in range(len(deallist)):
        roundmin = deallist[x]
        roundminkey = x
        for y in range(x,len(deallist)):
            if deallist[y] < roundmin:
                roundmin = deallist[y]
                roundminkey = y
        deallist[x],deallist[roundminkey] = deallist[roundminkey],deallist[x]
    return deallist