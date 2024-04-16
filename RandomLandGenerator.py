import random
from PIL import Image
#must be at least 10
lenX = int(input("give me a number that is more then 15: "))
lenY = lenX
if lenX < 15:
    lenX = 15
    lenY = 15

groundX = []
darkskyX = []
img = Image.new("RGB", (lenX,lenY), (135, 206, 235))

def genGroundList():
    global groundX, lenY, lenX
    hight = round(lenY*0.7)
    hight += random.randint(-3,3)
    for i in range(lenX):
        hight += random.randint(-1,1)
        groundX.append(hight)

def genDarkSkyList():
    global darkskyX, lenY, lenX

    hight = round(lenY/7)
    for i in range(lenX):
        hight += random.randint(-1,1)
        darkskyX.append(hight)

def genAddColorOutlines():
    global groundX, darkskyX, lenX, lenY
    for i in range(lenX):
        #grass
        img.putpixel((i, groundX[i]), (124, 252, 0))
        #darksky
        img.putpixel((i, darkskyX[i]), (70, 190, 240))

def genFillOutlines():
    global groundX, darkskyX, lenX, lenY
    #generate the dirt under the grass
    for i in range(len(groundX)):
        for j in range(groundX[i]+1, lenY):
            img.putpixel((i, j), (118,85,43))
    #generate a darker sky
    for i in range(len(darkskyX)):
        for j in range(darkskyX[i],):
            img.putpixel((i, j), (70, 190, 240))

def trees():
    global groundX,lenX,lenY
    xVal = random.randint(3,lenX-3)
    yVal = groundX[xVal]-1
    treeHight = 3
    #generate trunk
    for i in range(random.randint(3,10)):
      img.putpixel((xVal,yVal-i),(59, 38, 11))
      treeHight -= 1
    #img.putpixel((xVal, yVal-1), (59, 38, 11))
    #img.putpixel((xVal, yVal-2), (59, 38, 11))
    #generate leaves L2
    img.putpixel((xVal+1, yVal-(2-treeHight)), (96, 209, 36))
    img.putpixel((xVal+2, yVal-(2-treeHight)), (96, 209, 36))
    img.putpixel((xVal-1, yVal-(2-treeHight)), (96, 209, 36))
    img.putpixel((xVal-2, yVal-(2-treeHight)), (96, 209, 36))
    #generate leaves L2
    img.putpixel((xVal, yVal-(3-treeHight)), (96, 209, 36))
    img.putpixel((xVal+1, yVal-(3-treeHight)), (96, 209, 36))
    img.putpixel((xVal+2, yVal-(3-treeHight)), (96, 209, 36))
    img.putpixel((xVal-1, yVal-(3-treeHight)), (96, 209, 36))
    img.putpixel((xVal-2, yVal-(3-treeHight)), (96, 209, 36))
    #generate leaves L3 and 4
    img.putpixel((xVal, yVal - (4-treeHight)), (96, 209, 36))
    img.putpixel((xVal+1, yVal - (4-treeHight)), (96, 209, 36))
    img.putpixel((xVal-1, yVal - (4-treeHight)), (96, 209, 36))
    img.putpixel((xVal, yVal - (5-treeHight)), (96, 209, 36))


genGroundList()
genDarkSkyList()
genAddColorOutlines()
genFillOutlines()
for i in range(round(1),round(random.randint(1,round(lenX/5)))):
    trees()
img.show()
img.save("out.png")
