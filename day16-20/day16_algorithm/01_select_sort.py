#简单选择排序
#将第1个与后面n-1进行比较，如果后面n-1中有比当前的小，那么互换位置，然后进行第2个和后面n-2进行比较，依次下去

def select_sort(origin_items,comp=lambda x,y:x<y):
    items = origin_items[:]
    # print(items)
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]
    return items

def main():
    # items = input('输入排序数字以\',\'隔开：')
    # items = items.split(',')
    # origin_items = []
    # for i in items:
    #     origin_items.append(int(i))
    # print(type(origin_items))
    # print(origin_items)
    origin_items = [3,15,34,47,9,1]
    print(select_sort(origin_items))

if __name__ == '__main__':
    main()
