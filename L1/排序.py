# 冒泡排序
def bubble_sort(sort_lists: list):
    count = len(sort_lists) - 1
    for i in range(count, 0, -1):
        for j in range(i):
            if sort_lists[j] > sort_lists[j + 1]:
                sort_lists[j], sort_lists[j + 1] = sort_lists[j + 1], sort_lists[j]
    return sort_lists


sort_list = [9, 8, 23, 45, 1, 3, 6]
print(bubble_sort(sort_list))

# 快排
sxh = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j) ** len(m)
    if i == s:
        print(i)
        sxh.append(i)
print("100-999 的水仙花数：%s" % sxh)
