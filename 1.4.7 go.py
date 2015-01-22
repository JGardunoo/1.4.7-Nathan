import PIL
import matplotlib.pyplot as plt
import os.path              
#open picture of GoPro camera
directory = os.path.dirname(os.path.abspath(__file__))  
GoPro_file = os.path.join(directory, 'GoPro.jpg')
#show image
GoPro_img = PIL.Image.open(GoPro_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(GoPro_img, interpolation='none')
fig.show()

# Open, resize, and display GoPro logo
GoPro_logo_file = os.path.join(directory, 'GoPro_logo.jpg')
GoPro_logo_img = PIL.Image.open(GoPro_logo_file)
GoPro_logo_small = GoPro_logo_img.resize((160,110))
fig2,axes2 = plt.subplots(1, 1)
axes2.imshow(GoPro_logo_img)
fig2.show()

GoPro_img.paste(GoPro_logo_small, (360, 115))
fig3, axes3 = plt.subplots(1, 1)
axes3.imshow(GoPro_img, interpolation='none')

axes3.axis('off')
fig3.show()
