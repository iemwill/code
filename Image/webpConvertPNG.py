from PIL import Image
import os

directory = os.fsencode(__file__[:-17])
os.makedirs(os.path.join(directory, b'pngs'))
for file in os.listdir(directory):
    if file.endswith(b'.webp'): 
        im = Image.open(os.path.join(directory, file)).convert("RGB")
        im.save(os.path.join(directory, b'pngs\\', file[:-4] + b'.png'),"png")
        continue
