from PIL import Image
import numpy as np

def read_LSB(img):
    count = 0
    output = 0
    string = "Message: "
    bit = 0
    for row in img:
        for col in row:
            for color in col:
                if(bit >= 8):
                    string+=chr(output)
                    output = 0
                    bit = 0
                    count += 1
                if(ord(string[-1]) == 0):
                    break
                output = output | (color & 1) << bit
                bit += 1
    print(string)


def write_LSB(img, data):
    index = 0
    bit = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i,j])):
                if(bit >= 8):
                    index += 1
                    bit = 0
                if(index < len(data)):
                    img[i,j,k] = (img[i,j,k] & ~np.uint8(1)) | ((ord(data[index]) & (np.uint8(1) << bit)) >> bit)
                    bit += 1
                elif(index == len(data)):
                    img[i,j,k] = img[i,j,k] & ~np.uint8(1)
                    bit += 1
                else:
                    break


image = np.array(Image.open('new.bmp'))
img = np.copy(image)
read_LSB(img)
write_LSB(img, "Hello world!")
print(type(img[0,0,0]))



            
Image.fromarray(img).save("new.bmp")