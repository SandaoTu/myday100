"""
按值调用和按引用调用
"""

def double(arg):
    print('Before: ',arg)
    arg = arg*2
    print('After: ',arg)

def change(arg):
    print('Before',arg)
    arg.append('More data')
    print('After: ',arg)

def main():
    num = 10
    double(num)
    print('num:',num,'\n')
    say = 'Hello'
    double(say)
    print('say:',say,'\n')
    list = [1,2,3,4,4]
    double(list)
    print('list:',list,'\n')

    list2=[1,2,3,4,5]
    change(list2)
    print('list2:',list2)

if __name__ == '__main__':
    main()