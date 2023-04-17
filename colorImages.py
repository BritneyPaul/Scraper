import PIL
from PIL import Image
import requests
from io import BytesIO
import webcolors
import pandas as pd
import webcolors
 
 
# read images from URL
url = "https://www.fantasy-milos.com/slider/69/slider_image.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img

  
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def top_colos(image, n):
    # convert the image to rgb
    image = image.convert('RGB')
     
    # resize the image to 300 x 300
    image = image.resize((300,300))
     
    detected_colors =[]
    for x in range(image.width):
        for y in range(image.height):
            detected_colors.append(closest_colour(image.getpixel((x,y))))
    Series_Colors = pd.Series(detected_colors)
    output=Series_Colors.value_counts()/len(Series_Colors)
    return(output.head(n))
 
 
top_colos(img,10)