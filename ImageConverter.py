from PIL import Image
import cv2
from PIL import ImageFilter


# Resizeing image
def Resize():
    basewidth = 300
    img = Image.open('image.jpg')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('resized_image.jpg')


# Convert to black n white
def Black_White():
    img = Image.open('image.jpg')
    imgGray = img.convert('L')
    imgGray.save('image.jpg')

# Sharpen_image
def Sharpen():

    imageObject = Image.open("image.jpg");
    imageObject.show();
    sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
    sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);
    sharpened1.show();
    sharpened2.show();

# Blur_image
def Blur():
    img = cv2.imread('image.jpg') 
    blurImg = cv2.blur(img,(10,10)) 
    cv2.imshow('blurred image',blurImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






while True:
    print("*****IMAGE CONVERTER*****")

    i=int(input("1.Resize Image\n2.Convert to black and white image\n3.Sharpen Image\n4.Blur the image\n5.Exit from converter\nYour Choice:"))

    if i == 1:
        Resize()
    elif i == 2:
        Black_White()
    elif i == 3:
        Sharpen()
    elif i == 4:
        Blur()
    elif i == 5:
        break
    else: 
        print("Enter a valid option:")


