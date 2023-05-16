import struct

# def blur(inpFile,outFile):

def convolution(color, kernel, r, c):
    colorconv = (
        (kernel[0][0] * color[r - 1][c - 1])
        + (kernel[0][1] * color[r - 1][c])
        + (kernel[0][2] * color[r - 1][c + 1])
        + (kernel[1][0] * color[r][c - 1])
        + (kernel[1][1] * color[r][c])
        + (kernel[1][2] * color[r][c + 1])
        + (kernel[2][0] * color[r + 1][c - 1])
        + (kernel[2][1] * color[r + 1][c])
        + (kernel[2][2] * color[r + 1][c + 1])
    )
    # The value of colorconv will always be between ( 0 - 255)
    return colorconv


img = open(f"C:\\Users\\sammy\\Desktop\\Sample.bmp", "rb")
copyImg = open(f"C:\\Users\\sammy\\Desktop\\SampleBlurred.bmp", "r+b")
img.seek(18, 0)
width = struct.unpack("i", img.read(4))[0]
height = struct.unpack("i", img.read(4))[0]
img.seek(10, 0)
offset = struct.unpack("i", img.read(4))[0]
img.seek(offset, 0)                              # Location where Pixels Start
# Separating blue, green and red components of the pixel
blue = []
green = []
red = []
for i in range(height):
    bluetemp = []
    greentemp = []
    redtemp = []
    for j in range(width):
        bluetemp.append(int.from_bytes(img.read(1), "little"))
        greentemp.append(int.from_bytes(img.read(1), "little"))
        redtemp.append(int.from_bytes(img.read(1), "little"))
    blue.append(bluetemp)
    green.append(greentemp)
    red.append(redtemp)
kernel = [[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]]
copyImg.seek(offset, 0)                     # Setting the pointer to where the pixels Start in copy file
for row in range(height):
    for col in range(width):
        if (row == 0 or row == height - 1) or (col == 0 or col == width - 1):
            b = int(blue[row][col]).to_bytes(1, "little")
            g = int(green[row][col]).to_bytes(1, "little")
            r = int(red[row][col]).to_bytes(1, "little")
            copyImg.write(b)
            copyImg.write(g)
            copyImg.write(r)
        else:
            blueconv = int(convolution(blue, kernel, row, col)).to_bytes(1, "little")
            greenconv = int(convolution(green, kernel, row, col)).to_bytes(1, "little")
            redconv = int(convolution(red, kernel, row, col)).to_bytes(1, "little")
            # Converting Integer Values Back to Bytes and writing in Image File
            copyImg.write(blueconv)
            copyImg.write(greenconv)
            copyImg.write(redconv)
