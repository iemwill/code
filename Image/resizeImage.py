from PIL import Image

image = Image.open('flex-IT clothing_blue.png')
new_image = image.resize((1200, 628))
new_image.save('flex-IT clothing_blue_1200x628.png')