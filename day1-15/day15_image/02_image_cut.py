#裁剪图像
from PIL import Image

def main():
    image = Image.open('./res/1.jpg')
    rect = 80,20,310,360
    image.crop(rect).show()
    print(help(image.crop))
    print(type(rect))

if __name__ == '__main__':
    main()