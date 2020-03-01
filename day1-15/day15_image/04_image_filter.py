#图片滤镜
from PIL import Image,ImageFilter

def main():
    image = Image.open('./res/1.jpg')
    image.filter(ImageFilter.CONTOUR).show()

if __name__ == '__main__':
    main()