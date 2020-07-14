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
    
    font = ImageFont.truetype("arial.ttf", 100)
    text_w, text_h = draw.textsize(title, font)

    draw.text(((w - text_w) / 2, (h-100) - text_h), title, (255,255,255), font=font, stroke_width=2, stroke_fill='#eeda19')
    draw.text(((w - text_w) / 2, (h-50) - text_h), year, (255,255,255), font=font, stroke_width=2, stroke_fill='#eeda19')
    img.save(img_src)
    return img_src
             
## Loop through all images to add border and name

for i in glob.glob('*.jpg'):
  img = Image.open(i)
  add_grey_border = ImageOps.expand(img,border=50,fill='grey')
  add_black_border = ImageOps.expand(add_grey_border,border=300,fill='black')
  add_black_border.save('%s' % i)
  if i.startswith('AB'):
    title = "Aveen"
  elif i.startswith('OB'):
    title = "Olivia"  
  elif i.startswith('KB'):
    title = "Katie"
  year = re.findall("\d{4}", i)[0]
  add_title(i, title, year)


