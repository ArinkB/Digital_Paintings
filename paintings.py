import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
import glob
import re


# ## SINGLE IMAGE

# img = Image.open('Art/AB-2020 (2).jpg')
# add_grey_border = ImageOps.expand(img,border=50,fill='grey')
# add_black_border = ImageOps.expand(add_grey_border,border=300,fill='black')
# add_black_border.save('Art/imaged-with-border.png')

os.chdir('Art')

## Function to add Title to image

def add_title(img_src, title, year):

    img = Image.open(img_src, 'r')
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    title_font = ImageFont.truetype("arial.ttf", 80)
    year_font = ImageFont.truetype("arial.ttf", 65)
    title_w, title_h = draw.textsize(title, title_font)
    year_w, year_h = draw.textsize(year, year_font)

    draw.text(((w - title_w) / 2, (h-155) - title_h), title, (255,255,255), font=title_font, stroke_width=2, stroke_fill='#eeda19')
    draw.text(((w - year_w) / 2, (h-75) - year_h), year, (255,255,255), font=year_font, stroke_width=2, stroke_fill='#eeda19')
    img.save(img_src)
    return img_src
             
## Loop through all images to add border

for i in glob.glob('*.jpg'):
  img = Image.open(i)
  add_grey_border = ImageOps.expand(img,border=50,fill='grey')
  add_black_border = ImageOps.expand(add_grey_border,border=300,fill='black')
  add_black_border.save(i.replace('jpg', 'jpeg'))

## Loop through all images to add title and year

for i in glob.glob('*.jpeg'):
  if i.startswith('AB'):
    title = "Aveen"
  elif i.startswith('OB'):
    title = "Olivia"  
  elif i.startswith('KB'):
    title = "Katie"
  year = re.findall("\d{4}", i)[0]
  add_title(i, title, year)

## Move Art to appropiate folder for digital display

