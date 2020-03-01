"""
归并排序 分治算法
归并算法是稳定的排序算法
事件复杂度为 O(nlog(n)),空间复杂度为 O(N)

"""

def merge_sort(items,comp= lambda x,y:x<=y):
    # 归并算法
    if len(items)<2:
        return items[:]
    mid = len(items)//2
    left = merge_sort(items[:mid],comp)
    right = merge_sort(items[mid:],comp)
    return merge(left,right,comp)

def merge(items1,items2,comp):
    #合并，将两个有序列表合并成为一个有序列表
    items = []
    index1,index2 = 0,0
    while index1<len(items1) and index2<len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 +=1
        else:
            items.append(items2[index2])
            index2 +=1
    items +=items1[index1:]
    items +=items2[index2:]
    return items

def main():
    items = [1,3,6,5,8,9]
    print(merge_sort(items))

if __name__ == '__main__':
    main()