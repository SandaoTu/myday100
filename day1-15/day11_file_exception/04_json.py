#使用python的json模块可以将字典或列表以json格式保存到文件中
import json

def main():
    mydict ={
        'name':'郑仁伟',
        'age':18,
        'friends':['刘德华','郭富城'],
        'book':[
            {'name':'python开发','price':30},
            {'name':'java开发','price':35},
            {'name':'web开发','price':28}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

if __name__ == '__main__':
    main()