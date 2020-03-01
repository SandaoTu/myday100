#高质量冒泡排序（搅拌排序）
#进行正向和反向同时进行比较

def bubble_sort(origin_items,comp = lambda x,y:x>y):
    items = origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i,len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items)-2-i,i,-1):
                if comp(items[j-1],items[j]):
                    items[j-1],items[j] = items[j],items[j-1]
                    swapped = True
        if not swapped:
            break

        return items

def main():
    origin_items = [2,5,74,3,7,8]
    print(bubble_sort(origin_items))

if __name__ == '__main__':
    main()