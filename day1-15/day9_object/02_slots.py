#python是动态语言，如果给一个类示例化之后，可以在在程序运行时给对象绑定新的属性和方法
#如果需要限定自定义类型的对象只能绑定某些属性和方法时，可以在类中定义__slots__变量来进行限定
#注意__slots__只对当前类有效，对其子类不起作用

class Person(object):
    #限定person对象只能如下属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <16:
            print('%s正在玩跳字棋'%self._name)
        else:
            print('%s学习python'%self._name)

def main():
    person = Person('郑仁伟',18)
    person.play()
    person._gender = '男'
    print(person._gender)
    #AttributeError: 'Person' object has no attribute 'is_f=goodman'
    #person._is_goodman =True


if __name__ == '__main__':
    main()