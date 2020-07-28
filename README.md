# DIGITAL CHILDREN'S DRAWINGS / PAINTINGS
*Creating digital library of drawings/painting from 3 kids.* 

#### Arink Bertrand

I have piles of drawings and pictures from my kids that are just sitting in a box and collecting dust. What I'd like to do is create a digital library of their drawings  with border and title to show who and when were the art pieces made.
Eventually I would like to place a monitor with a frame on the wall and be able to view these as wall art in our home and create a python program to randomly pick an image from the folder for each kid, no repeat. 

### How to Run
- Download and install Python 3 (I used 3.7.6)
- Clone my repo
   - git bash at location you want to clone repo in
   - in git bash enter: git clone https://github.com/ArinkB/Digital_Paintings.git
- In the folder (Digital Paintings/Art) you will see some paintings done by my daughters, you can open these in any photo viewer/ editor to see its original state.
- Run paintings.py
- See section "What the code does now"
- You can see the changes in the Digital Paintings/Art folder


### My Plan of Action
- [x] Create Readme file to explain plan
- [x] Scan images from kids
- [x] Rename images to include kid name
- [x] Import necessary packages
- [ ] Plan to have 2 different displays for Vertical & Horizontal images
- [ ] Update ReadMe to futher explain varifications, language etc.
### Dependencies
-  Python v. 3.7.6
-  Import Os, Shutil 
-  Import PIL (Pillow) - Image, ImageOps, ImageDraw, ImageFont
-  Import glob
-  Import re

#### What the code does now:
After scanning and naming the images (manually), the script will:
- Place 2 borders around the image (currently black and grey).
- Display the child's name (based on the first 2 letters of the file name) and year it was drawn (based on file name using regex) at the bottom center of the image.
- Save the adjusted files as .jpeg while keeping the OG files .jpg
- Determine the size of the .jpeg files and if width is bigger than height it will move thoe files to the Landscape folder, while moving the others to portrait.
- Move all .jpg files to the OG folder so that duplicates are not made everytime new images are scanned and script is run.

#### Future steps:
As I learn more about python I would like to implement code to determine whether the monitor is set up vertically or horizontally, based on these the program will then display art from either the portrait or landscape foler.
