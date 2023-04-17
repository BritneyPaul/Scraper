# from PIL import Image
# import csv
# import urllib.request

# with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Decathlon_images.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         url = row[0]
#         try:
#             image = Image.open(urllib.request.urlopen(url))
#             image.show()
#         except:
#             print(f"Failed to open {url}")


# from PIL import Image
# import csv
# import urllib.request
# from colorthief import ColorThief

# with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Decathlon_images.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         url = row[0]
#         try:
#             image = Image.open(urllib.request.urlopen(url))
#             image.show()
#             color_thief = ColorThief(url)
#             dominant_color = color_thief.get_color(quality=1)
#             color_name = color_thief.get_color_name(dominant_color)
#             print(f"Dominant color in {url} is {color_name}")
#         except:
#             print(f"Failed to open {url}")


# import csv
# import urllib.request
# import numpy as np
# import cv2
# from collections import Counter
# from webcolors import rgb_to_name

# with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Decathlon_images.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         url = row[0]
#         try:
#             req = urllib.request.urlopen(url)
#             arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
#             img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             pixels = img.reshape((img.shape[0] * img.shape[1], 3))
#             colors = [tuple(pixel) for pixel in pixels]
#             dominant_colors = [color for color, _ in Counter(colors).most_common(2)]
#             # convert RGB tuples to color names using webcolors
#             color_names = [rgb_to_name(color) for color in dominant_colors]
#             print(f"Colors in {url}: {Counter(color_names)}")
#         except:
#             print(f"Failed to open {url}")


# from PIL import Image, ImageColor
# import csv
# import urllib.request
# from collections import Counter

# with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Decathlon_images.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         url = row[0]
#         try:
#             image = Image.open(urllib.request.urlopen(url))
#             colors = image.getcolors(image.size[0] * image.size[1])
#             dominant_colors = [ImageColor.getcolor(color[1], 'RGB') for color in sorted(colors, reverse=True)[:10]]
#             # The above line gets the top 10 most dominant colors in the image
#             print(f"Colors in {url}: {Counter(dominant_colors)}")
#         except:
#             print(f"Failed to open {url}")

# from PIL import Image
# import csv
# import urllib.request
# from concurrent.futures import ThreadPoolExecutor
# from scipy.spatial import KDTree
# from webcolors import (
#     CSS3_HEX_TO_NAMES,
#     hex_to_rgb,
# )

# def main():
#     with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Decathlon_images.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         urls = [row[0] for row in reader]

#     with ThreadPoolExecutor(max_workers=4) as executor:
#         results = executor.map(process_image, urls)

#     for url, colors in results:
#         print(f"Colors in {url}: {colors}")

# def convert_rgb_to_names(rgb_tuple):
    
#     # a dictionary of all the hex and their respective names in css3
#     css3_db = CSS3_HEX_TO_NAMES
#     names = []
#     rgb_values = []
#     for color_hex, color_name in css3_db.items():
#         names.append(color_name)
#         rgb_values.append(hex_to_rgb(color_hex))
    
#     kdt_db = KDTree(rgb_values)
#     index = kdt_db.query(rgb_tuple)
#     return f'closest match: {names[index]}'

# def process_image(url):
#     try:
#         image = Image.open(urllib.request.urlopen(url))
#         image = image.resize((image.size[0]//2, image.size[1]//2)) # Resize the image
#         pixels = image.load()
#         all_colors = (pixels[i, j] for i in range(image.size[0]) for j in range(image.size[1]))
#         dominant_colors = list(set(all_colors))[:2] # Get a list of unique dominant colors
#         return (url, dominant_colors)
#     except:
#         return (url, None)


# if __name__ == '__main__':
#     main()            


# from PIL import Image
# import csv
# import urllib.request
# from collections import Counter
# from concurrent.futures import ThreadPoolExecutor
# from webcolors import rgb_to_name

# def main():
#     with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Bol_images.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         urls = [row[0] for row in reader]

#     with ThreadPoolExecutor(max_workers=4) as executor:
#         results = executor.map(process_image, urls)

#     for url, colors in results:
#         print(f"Colors in {url}: {colors}")

# def process_image(url):
#     try:
#         image = Image.open(urllib.request.urlopen(url))
#         image = image.resize((image.size[0]//2, image.size[1]//2)) # Resize the image
#         pixels = image.load()
#         all_colors = (pixels[i, j] for i in range(image.size[0]) for j in range(image.size[1]))
#         dominant_colors = [rgb_to_name(color) for color, _ in Counter(all_colors).most_common(2)]
#         return (url, Counter(dominant_colors))
#     except Exception as e:
#         print(f"Error processing {url}: {e}")
#         return (url, None)


# if __name__ == '__main__':
#     main()

# import csv
# import os
# import urllib.request
# from collections import Counter
# from concurrent.futures import ThreadPoolExecutor
# from PIL import Image
# from webcolors import rgb_to_name

# # Define a function to get the image URLs from a CSV file
# def get_image_urls(filepath):
#     with open(filepath, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         urls = [row[0] for row in reader]
#     return urls

# def process_image(url):
#     try:
#         image = Image.open(urllib.request.urlopen(url))
#         image = image.resize((image.size[0]//2, image.size[1]//2)) # Resize the image
#         pixels = image.load()
#         all_colors = [pixels[i, j] for i in range(image.size[0]) for j in range(image.size[1])]
#         dominant_colors = [rgb_to_name(color) for color, _ in Counter(all_colors).most_common(2)]
#         return (url, Counter(dominant_colors))
#     except Exception as e:
#         print(f"Error processing {url}: {e}")
#         return (url, None)

# def main():
#     # Define directory path where the CSV files are located
#     dir_path = 'C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/'

#     # Loop over file names and process each file
#     for filename in ['Bol_images.csv', 'Decathlon_images.csv', 'Wehkamp_images.csv']:
#         # Get the full file path
#         filepath = os.path.join(dir_path, filename)
        
#         # Get the image URLs from the CSV file
#         urls = get_image_urls(filepath)

#         # Process the images
#         with ThreadPoolExecutor(max_workers=4) as executor:
#             results = executor.map(process_image, urls)

#         # Print the results
#         for url, colors in results:
#             if colors is not None:
#                 print(f"Colors in {url}: {colors}")

# if __name__ == '__main__':
#     main()

import os
import urllib.request
import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from webcolors import rgb_to_name
import pyodbc

# Define a function to get the image URLs from a CSV file
def get_image_urls(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        urls = [row[0] for row in reader]
    return urls

def process_image(url):
    try:
        image = Image.open(urllib.request.urlopen(url))
        image = image.resize((image.size[0]//2, image.size[1]//2)) # Resize the image
        pixels = image.load()
        all_colors = [pixels[i, j] for i in range(image.size[0]) for j in range(image.size[1])]
        dominant_colors = [rgb_to_name(color) for color, _ in Counter(all_colors).most_common(2)]
        return (url, dominant_colors)
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return (url, None)

def insert_colors(url, colors):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=BRITNEY;DATABASE=DEDSW9db;UID=BRITNEY/bpaul')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images_color (url, color1, color2) VALUES (?, ?, ?)", url, colors[0], colors[1])
    cursor.commit()
    cursor.close()
    conn.close()

def main():
    # Define directory path where the CSV files are located
    dir_path = 'C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/'

    # Loop over file names and process each file
    for filename in ['Bol_images.csv', 'Decathlon_images.csv', 'Wehkamp_images.csv']:
        # Get the full file path
        filepath = os.path.join(dir_path, filename)
        
        # Get the image URLs from the CSV file
        urls = get_image_urls(filepath)

        # Process the images
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = executor.map(process_image, urls)

        # Insert the results into the database
        for url, colors in results:
            if colors is not None:
                insert_colors(url, colors)

if __name__ == '__main__':
    main()


