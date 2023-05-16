import struct
class Edit_tools :
    def grayScale(self,inpFile,outFile):
        # inpFile=open("C:\\Users\\saimy\\Desktop\\sample22.bmp","rb")
        # inpFile=open("C:\\Users\\saimy\\Desktop\\sample22.bmp","rb")
        # inpFile=open("C:\\Users\\saimy\\Desktop\\sample22.bmp","rb")
        # outFile=open("C:\\Users\\saimy\\Desktop\\sampleCopy.bmp","r+b")
        inpFile.seek(2)                                     # Skipping Signature Bytes
        print("FileSize is",struct.unpack('i',inpFile.read(4))[0],"kb")
        inpFile.seek(10)                                    # Skipping Reserved Bytes
        pix=struct.unpack('i',inpFile.read(4))
        inpFile.seek(18)                                    # Putting pointer at where Width and height is written
        width=struct.unpack('i',inpFile.read(4))[0]
        print("Width in Pixels :",width)
        height=struct.unpack('i',inpFile.read(4))[0]
        print("Height in Pixels :",height)
        # outFile=open("C:\\Users\\saimy\\Desktop\\sampleCopy.bmp","r+b")            # Used r+b to read and write Both in binary
        inpFile.seek(pix[0])                                # Setting file pointer to the very first pixel value(pix)
        outFile.seek(pix[0])                                # Setting file pointer to the very first pixel value(pix)
        print("\nPlease Wait...")

        for i in range(height):
            for j in range(width):
                b=int.from_bytes(inpFile.read(1),"little")
                g=int.from_bytes(inpFile.read(1),"little")
                r=int.from_bytes(inpFile.read(1),"little")
                grayScInt=int((b+g+r)/3)
                grayScByt=grayScInt.to_bytes(1,"little")     # Converting integer value back to bytes before writing in file
                outFile.write(grayScByt)
                outFile.write(grayScByt)
                outFile.write(grayScByt)

        inpFile.close()
        outFile.close()
        print("Done")
    
    def edgeDetect(self,inpFile,outFile):
        def Keepinrange(value):
            # Making Sure Values Stays in the Range ( 0 - 255 )
            if value < 0:
                return 0
            elif value > 255:
                return 255
            else:
                return value
        def convolution(color, kernel, r, c):
            # Multiplying pixel and its Surrounding 8 Pixels by their corresponding Kernel Values
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
            return int(colorconv)

        # inpFile = open(f"C:\\Users\\saimy\\Desktop\\sample22.bmp", "rb")
        # outFile = open(f"C:\\Users\\saimy\\Desktop\\sampleCopy.bmp", "r+b")
        inpFile.seek(18, 0)
        width = struct.unpack("i", inpFile.read(4))[0]
        height = struct.unpack("i", inpFile.read(4))[0]
        inpFile.seek(10, 0)
        offset = struct.unpack("i", inpFile.read(4))[0]
        inpFile.seek(offset, 0)
        # Separating blue, green and red components of the pixel
        blue = []
        green = []
        red = []
        for i in range(height):
            bluetemp = []
            greentemp = []
            redtemp = []
            for j in range(width):
                bluetemp.append(int.from_bytes(inpFile.read(1), "little"))
                greentemp.append(int.from_bytes(inpFile.read(1), "little"))
                redtemp.append(int.from_bytes(inpFile.read(1), "little"))
            blue.append(bluetemp)
            green.append(greentemp)
            red.append(redtemp)
        # Applying  Sharpening
        kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        outFile.seek(offset, 0)                   # Setting the pointer to where the pixels Start in copy file
        for row in range(height):
            for col in range(width):
                if (row == 0 or row == height - 1) or (col == 0 or col == width - 1):
                    b = int(blue[row][col]).to_bytes(1, "little")
                    g = int(green[row][col]).to_bytes(1, "little")
                    r = int(red[row][col]).to_bytes(1, "little")
                    outFile.write(b)
                    outFile.write(g)
                    outFile.write(r)
                else:
                    blueconv = Keepinrange(convolution(blue, kernel, row, col))
                    greenconv = Keepinrange(convolution(green, kernel, row, col))
                    redconv = Keepinrange(convolution(red, kernel, row, col))
                    # Converting Integer Values Back to Bytes and writing in Image File
                    outFile.write(blueconv.to_bytes(1,"little"))
                    outFile.write(greenconv.to_bytes(1,"little"))
                    outFile.write(redconv.to_bytes(1,"little"))
    def negative(self,inpFile,outFile):
        inpFile.seek(2)                                 # Skipping Signature Bytes
        print("FileSize is",struct.unpack('i',inpFile.read(4))[0],"kb")
        inpFile.seek(10)                                # Skipping Reserved Bytes
        pix=struct.unpack('i',inpFile.read(4))          # The Location of pixels is stored in [ pix ]
        inpFile.seek(18)                                # Putting pointer at where Width and height is written
        width=struct.unpack('i',inpFile.read(4))[0]
        print("Width in Pixels :",width)
        height=struct.unpack('i',inpFile.read(4))[0]
        print("Height in Pixels :",height)
        inpFile.seek(pix[0])                            # Setting file pointer to the very first pixel value(pix)
        outFile.seek(pix[0])                            # Setting file pointer to the very first pixel value(pix)
        print("\nPlease Wait...")

        for i in range(height):
            for j in range(width):
                b=int.from_bytes(inpFile.read(1),"little")
                g=int.from_bytes(inpFile.read(1),"little")
                r=int.from_bytes(inpFile.read(1),"little")
                # subtracting b , g , r values from 255 to get negative of the image
                neg_b=abs(255 - b)
                neg_g=abs(255 - g)
                neg_r=abs(255 - r)
                # Converting integer values back to bytes
                outFile.write(neg_b.to_bytes(1, "little"))
                outFile.write(neg_g.to_bytes(1, "little"))
                outFile.write(neg_r.to_bytes(1, "little"))

        inpFile.close()
        outFile.close()
        print("Done")


    def emboss(self,inpFile,outFile):
        def Keepinrange(value):
            # Making Sure Values Stays in the Range ( 0 - 255 )
            if value < 0:
                return 0
            elif value > 255:
                return 255
            else:
                return value
        def convolution(color, kernel, r, c):
            # Multiplying pixel and its Surrounding 8 Pixels by their corresponding Kernel Values
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
            return int(colorconv+137)

        inpFile.seek(18, 0)
        width = struct.unpack("i", inpFile.read(4))[0]
        height = struct.unpack("i", inpFile.read(4))[0]
        inpFile.seek(10, 0)
        offset = struct.unpack("i", inpFile.read(4))[0]
        inpFile.seek(offset, 0)
        # Separating blue, green and red components of the pixel
        blue = []
        green = []
        red = []
        for i in range(height):
            bluetemp = []
            greentemp = []
            redtemp = []
            for j in range(width):
                bluetemp.append(int.from_bytes(inpFile.read(1), "little"))
                greentemp.append(int.from_bytes(inpFile.read(1), "little"))
                redtemp.append(int.from_bytes(inpFile.read(1), "little"))
            blue.append(bluetemp)
            green.append(greentemp)
            red.append(redtemp)
        # Applying  Sharpening
        kernel = [[-1, 0, 0], [0, 0, 0], [0, 0, 1]]
        outFile.seek(offset, 0)                   # Setting the pointer to where the pixels Start in copy file
        for row in range(height):
            for col in range(width):
                if (row == 0 or row == height - 1) or (col == 0 or col == width - 1):
                    b = int(blue[row][col]).to_bytes(1, "little")
                    g = int(green[row][col]).to_bytes(1, "little")
                    r = int(red[row][col]).to_bytes(1, "little")
                    outFile.write(b)
                    outFile.write(g)
                    outFile.write(r)
                else:
                    blueconv = Keepinrange(convolution(blue, kernel, row, col))
                    greenconv = Keepinrange(convolution(green, kernel, row, col))
                    redconv = Keepinrange(convolution(red, kernel, row, col))
                    # Converting Integer Values Back to Bytes and writing in Image File
                    outFile.write(blueconv.to_bytes(1,"little"))
                    outFile.write(greenconv.to_bytes(1,"little"))
                    outFile.write(redconv.to_bytes(1,"little"))

# p = Edit_tools()
# inp=open("C:\\Users\\saimy\\Desktop\\sample22.bmp","rb")
# out=open("C:\\Users\\saimy\\Desktop\\sampleCopy.bmp","r+b")

# p.grayScale(inp,out)