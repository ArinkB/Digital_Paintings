import os
from PIL import Image, ImageOps
import glob

img = Image.open('Art/AB-2020(2).jpg')
add_grey_border = ImageOps.expand(img,border=50,fill='grey')
add_black_border = ImageOps.expand(add_grey_border,border=300,fill='black')
add_plaque = 
add_black_border.save('imaged-with-border.png')

# os.chdir('Art')

# for i in glob.glob('*.jpg'):
#   img = Image.open(i)
#   add_grey_border = ImageOps.expand(img,border=50,fill='grey')
#   add_black_border = ImageOps.expand(add_grey_border,border=300,fill='black')
#   add_black_border.save('%s' % i)


