#使用@property装饰器#
# @property装饰器将一个方法变为属性调用
#@property装饰器，同时会产生一个@  .setter装饰器

class Student(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age

    #访问器getter方法
    @property
    def name(self):
        return self._name

    #访问器 getter方法
    @property
    def age(self):
        return self._age

    #修改器 setter方法
    @age.setter
    def age(self,age):
        self._age = age

    def study(self):
        if self._age <16:
            print('正在学习数学')
        else:
            print('正在学习python')

def main():
    student = Student('张三',12)
    student.study()
    student.age = 18
    student.name1 = 'ni'
    student.study()
   # student.name = 'nihao' #name属性只有读的功能，age属性具有读写功能

if __name__ == '__main__':
    main()