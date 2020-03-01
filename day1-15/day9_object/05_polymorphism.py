#多态
#使用abc模块和ABCMeta元类和abstractmethod包装器实现抽象类效果
#抽象类不能够被实例化

from abc import ABCMeta , abstractmethod

class Pet(object, metaclass = ABCMeta):

    def __init__(self,nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s：汪汪汪...'%self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s:喵喵喵...'%self._nickname)


def main():
    pet = [Dog('旺财'),Cat('小花'),Dog('大黄')]
    for p in pet:
        p.make_voice()

if __name__ == '__main__':
    main()