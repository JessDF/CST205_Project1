file = pickAFile()
picture = makePicture(file)
def half(picture):
  height = getHeight(picture)
  width = getWidth(picture)
 # filters quadrant two
  for x in range (int (width/2), int(width)):
    for y in range (0, height/2):
     # def decreaseRed(picture):
          p = getPixel(picture, x, y)
         #creates a red filter in the 2nd quadrant.
          value= getRed(p)
          setRed(p,value*0.5)
#filters quadrant three
  for x in range (0, (width / 2)):
    for y in range (height / 2, height - 2):
      pixel = getPixelAt(picture, x, y)
      level = 255 - int(0.21*getRed(pixel) + 0.71*getGreen(pixel) +0.07*getBlue(pixel))
    #makes image grayscale.
      color = makeColor(level, level, level)
      setColor(pixel, color) 
#filters quadrant four
  for x in range ((width / 2), width):
    for y in range ((height / 2), height):     
      pixel = getPixelAt(picture, x, y)
      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)
   #This filter makes the image negative
      negColor = makeColor(255 - red, 255 - green, 255 - blue)
      setColor(pixel, negColor)             
half(picture)
repaint(picture)
show(picture)
