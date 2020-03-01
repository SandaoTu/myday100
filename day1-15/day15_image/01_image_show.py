#显示图像

from PIL import Image

def main():
    image = Image.open('./res/1.jpg')
    image.show()

if __name__ == '__main__':
    main()
