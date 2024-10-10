from bmp_io import BMPImageReader as ImRead
from bmp_io import BMPImageWriter as ImWrite

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


image = ImRead.from_file("new.bmp").pixel_array
img = np.copy(image)
write_LSB(img, "Hello world!")
ImWrite.arr_to_file(img, "new.bmp")
img = ImRead.from_file("new.bmp").pixel_array
read_LSB(img)