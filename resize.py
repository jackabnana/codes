import PIL
import os
import os.path
from PIL import Image

f = r'/home/sanjeep/Desktop/tesst/product2 image'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((500,500))
    img.save(f_img)
