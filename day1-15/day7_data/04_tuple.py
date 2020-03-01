import sys

num_tuple = (i for i in range(100))
num_list = [i for i in range(100)]

#查看元组和列表占用内存空间的大小
print(sys.getsizeof(num_tuple))
print(sys.getsizeof(num_list))