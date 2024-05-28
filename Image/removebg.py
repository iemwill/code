from rembg import remove
from PIL import Image

im = Image.open('flex-IT white bg.png')
remim = remove(im)
remim.save('flex-IT white bg removedbg.png',"png")