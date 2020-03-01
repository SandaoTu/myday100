import sys

f = [x for x in range(10)]
print(f)

f = [x+y for x in 'ABCD' for y in '123']
print(f)

f = [x**2 for x in range(1,100)]
print(sys.getsizeof(f))
print(f)
#注意以下是生成器对象
f = (x**2 for x in range(1,100))
print(sys.getsizeof(f))
for val in f:
    print(val)

