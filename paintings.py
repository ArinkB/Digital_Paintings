import os
from PIL import Image, ImageOps

# # img = Image.open('Art/AB-2020.jpg')
# # img_with_border = ImageOps.expand(img,border=300,fill='black')
# # img_with_border.save('imaged-with-border.png')

path = open('Art')
for i in os.listdir(path):
  img = Image.open(i)
  img_with_border = ImageOps.expand(img,border=300,fill='black')
  img_with_border.save

