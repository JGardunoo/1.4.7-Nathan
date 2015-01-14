import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
GoPro_file = os.path.join(directory, 'GoPro.jpg')

GoPro_img = PIL.Image.open(GoPro_file)
fig, ax = plt.subplots(1, 1)
ax.axis('off')
ax.imshow(GoPro_img, interpolation='none')

fig.show()

