#定义一个学生类

class Student(object):
    #__init__是一个特殊方法用于在创建对象的时候进行初始化
    #通过这个方法我们可以为学生这个对象绑定name和age两个属性
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在学习%s'%(self.name,course_name))

    #PEP8要求标识符的名字由小写字母和下划线组成
    def watch_movie(self):
        if self.age<18:
            print('%s只能观看《熊出没》'%self.name)
        else:
            print('%s观看动作大片'%self.name)

def main():
    #创建学生对象并指定姓名和年龄
    stu1 = Student('郑仁伟',18)
    #给对象发study消息
    stu1.study('Python编程')
    #给对象发送watch movie消息
    stu1.watch_movie()

    stu2 = Student('王大锤',28)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
    main()