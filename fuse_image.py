from PIL import Image
from urllib.request import urlopen
import urllib.error
import os

hc_logo = 'http://cityread.london/wp-content/uploads/2016/02/HarperCollins-logo.png'

def fuse_logo(url,img_id):
    # IMAGE - from input url
    image = Image.open(urlopen(url))

    # HC LOGO
    logo = Image.open(urlopen(hc_logo)).convert('RGBA')

    # CROPPING THE HC LOGO
    # Setting the points for cropped image
    left = 197
    top = 165
    right = 540
    bottom = 560

    logo_cropped = logo.crop((left, top, right, bottom))
    # Resizing the cropped logo
    logo_cr_resized = logo_cropped. resize ((180,180))
    # Copying the final logo
    logo_copy = logo_cr_resized.copy()

    # Making a Copy of the URL Image
    image_copy = image.copy()

    # Position parameters for the logo on the URL image
    position = ((image_copy.width - logo.width), (image_copy.height - logo.height))

    # PASTING LOGO ON URL IMAGE
    image_copy.paste(logo_copy, (0,(image_copy.height-200)), logo_copy)

    # # SAVING FINAL IMAGE To DIRECTORY
    save_path = './fusion/'+str(img_id)+'.jpg'
    image_copy.save(save_path)
    final_image = save_path

    # Return the directory path
    return final_image
