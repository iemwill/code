from rembg import remove
from PIL import Image
import os

directory = os.fsencode(__file__[:-11])
os.makedirs(os.path.join(directory, b'removedBackGround'))
for file in os.listdir(directory):
    if file.endswith(b'.png'): 
        im = Image.open(os.path.join(directory, file))
        remim = remove(im)
        remim.save(os.path.join(directory, b'removedBackGround\\', file[:-4] + b'.png'),"png")
        continue