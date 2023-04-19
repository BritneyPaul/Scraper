
# import PIL
# from PIL import Image
# import requests
# from io import BytesIO
# import webcolors
# import pandas as pd

# # read file containing image URLs
# with open('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/Bol_images.csv') as bol:
#     urls = bol.read().splitlines()

# def closest_colour(requested_colour):
#     min_colours = {}
#     for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_colour[0]) ** 2
#         gd = (g_c - requested_colour[1]) ** 2
#         bd = (b_c - requested_colour[2]) ** 2
#         min_colours[(rd + gd + bd)] = name
#     return min_colours[min(min_colours.keys())]

# def top_colors(image, n):
#     # convert the image to rgb
#     image = image.convert('RGB')

#     # resize the image to 300 x 300
#     image = image.resize((10,10))

#     detected_colors =[]
#     for x in range(image.width):
#         for y in range(image.height):
#             detected_colors.append(closest_colour(image.getpixel((x,y))))
#     Series_Colors = pd.Series(detected_colors)
#     output=Series_Colors.value_counts()/len(Series_Colors)
#     return(output.head(n))

# for url in urls:
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     print(top_colors(img, 10))

# import os
# import pyodbc
# from sqlalchemy import create_engine
# import pandas as pd
# import requests
# from io import BytesIO
# from PIL import Image
# import webcolors

# # Define the connection details for the SQL Server database
# server_name = 'BRITNEY'
# database_name = 'reviewAnalysis'
# driver = '{ODBC Driver 17 for SQL Server}'

# # Create a SQLAlchemy engine object
# engine = create_engine(f"mssql+pyodbc://{server_name}/{database_name}?driver={driver}")

# # Create a pyodbc connection object
# connection = pyodbc.connect(f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes")

# # function to find closest color name from RGB value
# def closest_color(requested_color):
#     min_colors = {}
#     for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_color[0]) ** 2
#         gd = (g_c - requested_color[1]) ** 2
#         bd = (b_c - requested_color[2]) ** 2
#         min_colors[(rd + gd + bd)] = name
#     return min_colors[min(min_colors.keys())]

# # function to print top colors in an image
# def print_top_colors(image_url, n):
#     response = requests.get(image_url)
#     img = Image.open(BytesIO(response.content))
#     # resize the image to 300 x 300
#     img = img.resize((300, 300))
#     detected_colors = []
#     for x in range(img.width):
#         for y in range(img.height):
#             detected_colors.append(closest_color(img.getpixel((x,y))))
#     series_colors = pd.Series(detected_colors)
#     output = series_colors.value_counts()/len(series_colors)
#     print(f"Top {n} colors in {image_url}:")
#     print(output.head(n))
#     print("=" * 30)

# # change directory to where the CSV files are located
# os.chdir('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/') #C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/Bol_reviews.csv

# # loop over each CSV file in the directory
# for filename in os.listdir():
#     if filename.endswith('.csv'):
#         with open(filename, 'r') as csv_file:
#             urls = csv_file.read().splitlines()
#         for url in urls:
#             print_top_colors(url, 1)


# # Insert the results into the SQL Server table      
#         cursor = connection.cursor()
#         for index, row in df.iterrows():
#             imageurl = row['image']
#             sentiment = row['sentiment_label']
#             query = "INSERT INTO dbo.Kleur (Image_url, color) VALUES (?, ?)"
#             cursor.execute(query, imageurl, sentiment)
#             connection.commit()

#  # Print a message to indicate that the results have been inserted into the database
#         print(f"Sentiment analysis results for file '{file_name}' have been inserted into the database.")
#         print()

# # Close the connection
# connection.close()


# import os
# import pyodbc
# from sqlalchemy import create_engine
# import pandas as pd
# import requests
# from io import BytesIO
# from PIL import Image
# import webcolors

# # Define the connection details for the SQL Server database
# server_name = 'BRITNEY'
# database_name = 'colorAnalysis'
# driver = '{ODBC Driver 17 for SQL Server}'

# # Create a SQLAlchemy engine object
# engine = create_engine(f"mssql+pyodbc://{server_name}/{database_name}?driver={driver}")

# # Create a pyodbc connection object
# connection = pyodbc.connect(f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes")

# # function to find closest color name from RGB value
# def closest_color(requested_color):
#     min_colors = {}
#     for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
#         r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#         rd = (r_c - requested_color[0]) ** 2
#         gd = (g_c - requested_color[1]) ** 2
#         bd = (b_c - requested_color[2]) ** 2
#         min_colors[(rd + gd + bd)] = name
#     return min_colors[min(min_colors.keys())]

# # function to print top colors in an image
# def print_top_colors(image_url, n):
#     response = requests.get(image_url)
#     img = Image.open(BytesIO(response.content))
#     # resize the image to 300 x 300
#     img = img.resize((10, 10))
#     detected_colors = []
#     for x in range(img.width):
#         for y in range(img.height):
#             detected_colors.append(closest_color(img.getpixel((x,y))))
#     series_colors = pd.Series(detected_colors)
#     output = series_colors.value_counts()/len(series_colors)
#     return output.head(n)

# # change directory to where the CSV files are located
# os.chdir('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/')

# # loop over each CSV file in the directory
# for filename in os.listdir():
#     if filename.endswith('.csv'):
#         with open(filename, 'r') as csv_file:
#             urls = csv_file.read().splitlines()
#             urls = csv_file.readlines()[1:] #skips first line of csv file



#             results = []
#             for url in urls:
#                 top_colors = print_top_colors(url, 1)
#                 results.append((url, top_colors.index[0]))

#             # Insert the results into the SQL Server table
#             cursor = connection.cursor()
#             for result in results:
#                 imageurl = result[0]
#                 color = result[1]
#                 query = "INSERT INTO dbo.Kleur (Image_url, color) VALUES (?, ?)"
#                 cursor.execute(query, (imageurl, color))
#                 connection.commit()
import os
import pyodbc
from sqlalchemy import create_engine
import pandas as pd
import requests
from io import BytesIO
from PIL import Image
import webcolors


# Define the connection details for the SQL Server database
server_name = 'BRITNEY'
database_name = 'colorAnalysis'
driver = '{ODBC Driver 17 for SQL Server}'

# Create a SQLAlchemy engine object
engine = create_engine(f"mssql+pyodbc://{server_name}/{database_name}?driver={driver}")

# Create a pyodbc connection object
conn = pyodbc.connect(f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes")

# function to find closest color name from RGB value
def closest_color(requested_color):
    excluded_ranges = [
        ((220, 220, 220), (255, 255, 255)),  # white and light gray range
        ((245, 245, 220), (255, 250, 205)),  # beige range
        ((173, 216, 230), (224, 255, 255)),  # light blue range
        ((255, 239, 213), (255, 249, 231)),  # papayawhip range
        ((250, 235, 215), (255, 239, 219)),  # antique range
        ((211, 211, 211), (211, 211, 211)),  # lightgray range
    ]
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        rgb = webcolors.hex_to_rgb(key)
        if any(
            r_min <= rgb[0] <= r_max and
            g_min <= rgb[1] <= g_max and
            b_min <= rgb[2] <= b_max
            for (r_min, g_min, b_min), (r_max, g_max, b_max) in excluded_ranges
        ):
            continue
        rd = (rgb[0] - requested_color[0]) ** 2
        gd = (rgb[1] - requested_color[1]) ** 2
        bd = (rgb[2] - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]




# function to print top colors in an image
def print_top_colors(image_url, n):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    # resize the image to 300 x 300
    img = img.resize((10, 10))
    detected_colors = []
    for x in range(img.width):
        for y in range(img.height):
            detected_colors.append(closest_color(img.getpixel((x,y))))
    series_colors = pd.Series(detected_colors)
    output = series_colors.value_counts()/len(series_colors)
    print(f"Top {n} colors in {image_url}:")
    print(output.head(n))
    print("=" * 30)

# change directory to where the CSV files are located
os.chdir('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/images/') #C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/Bol_reviews.csv

# loop over each CSV file in the directory
for filename in os.listdir():
    if filename.endswith('.csv'):
        with open(filename, 'r') as csv_file:
            urls = csv_file.read().splitlines()[1:]
            # urls = csv_file.readlines()[1:] #skips first line of csv file
        for url in urls:
            top_color = closest_color(Image.open(BytesIO(requests.get(url).content)).getpixel((0,0)))
            query = f"INSERT INTO Kleur (Image_url, color) VALUES ('{url}', '{top_color}')"
            conn.execute(query)
            conn.commit()

