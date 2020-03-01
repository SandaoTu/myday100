#读写二进制文件

def main():
    try:
        with open('ball.png','rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('球.png','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开')
    except IOError:
        print('读写文件时出现错误')
    print('程序执行结束')

if __name__ == '__main__':
    main()