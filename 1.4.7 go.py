import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
GoPro-Hero-4_file = os.path.join(directory, 'GoPro-Hero-4.jpg')

GoPro-Hero-4_img = PIL.Image.open(GoPro-Hero-4_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(GoPro-Hero-4_img, interpolation='none')
