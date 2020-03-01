"""
穷举法:又称暴力破解法，将所有可能的情况进行验证，直到找到正确答案
例子：百元百鸡，五人分鱼
"""
def exhaustion1():
    # 百元白鸡问题,公鸡5元一只，母鸡3元一只，小鸡一元三只
    #请问，用100元买100只鸡，公鸡/母鸡/小鸡分别是多少？
    #100=5*x+3*y+z/3
    for x in range(20):
        for y in range(33):
            z = 100 -x -y
            if 5*x+3*y+z//3 == 100 and z %3 == 0:
                print(x,y,z)
def exhaustino2():
    pass

def main():
    exhaustion1()

if __name__ == '__main__':
    main()
