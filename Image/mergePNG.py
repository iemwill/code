import os
from PIL import Image

directory = os.getcwd()
parentDirectory = os.path.dirname(directory)

for file in os.listdir(os.path.join(parentDirectory, 'removedBackGround')):
	background = Image.open(os.path.join(directory, 'background.png'))
	background = background.resize((823, 823))
	foreground = Image.open(os.path.join(parentDirectory, 'removedBackGround\\', file))
	foreground = foreground.resize((823, 823))
	background.paste(foreground, (0, 0), foreground)
	background.save(os.path.join(directory, file[:-4] + 'NB.png'),"png")
	continue