#读写文本文件

def main():
    f = open('test.txt','r',encoding='utf-8')
    print(f.read())
    # help(f)
    f.close()

if __name__ == '__main__':
    main()