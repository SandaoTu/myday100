#生成缩略图
from PIL import Image

def main():
    image = Image.open('./res/1.jpg')
    size = 128,128
    image.thumbnail(size)
    image.show()

if __name__ == '__main__':
    main()