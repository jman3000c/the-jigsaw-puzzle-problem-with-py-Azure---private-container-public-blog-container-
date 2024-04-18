from PIL import Image
import os
import numpy as np
import pandas as pd
from openpyxl import Workbook

def calculate_edge_sums(image):
    # Convert the image to a NumPy array
    data = np.array(image)

    # Calculate the sum of the RGBA values for each edge
    left = np.sum(data[:, 0]) - 10200
    right = np.sum(data[:, -1]) - 10200
    top = np.sum(data[0, :]) - 10200
    bottom = np.sum(data[-1, :]) - 10200

    return left, top, right, bottom, False

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Define the image size
image_size = (40, 30)

# Define the size of each tile
tile_size = (40, 40)  # You may need to adjust this based on the size of your tiles

# Create a new image of the size required for the mosaic
mosaic = Image.new('RGB', (image_size[0]*tile_size[0], image_size[1]*tile_size[1]))

# Initialize an empty list to store the edge sums for each image
edge_sums = []
# img = Image.open('images/(1).png')
# data = np.array(img)
# Open the file in write mode ('w')
# with open('output.txt', 'w') as f:
#     # Write each item from the data list to the file
#     for item in data:
#         f.write("%s\n" % item)

# Loop through the images
for i in range(1, 1201):
    # Open the image file
    img = Image.open(f'images/({i}).png')
    # Calculate the edge sums for the current image and append to the list
    edge_sums.append(calculate_edge_sums(img))
    # Calculate the position in the mosaic where this image will be placed
    pos = ((i-1)%image_size[0]*tile_size[0], (i-1)//image_size[0]*tile_size[1])
    # Paste the current image into the mosaic
    mosaic.paste(img, pos)

pos_array=np.zeros(1200)
pos_array=[-1 for _ in pos_array]

corner_edge=0

    
for i in range(0, 1200):
    if edge_sums[i][4] == False :
        if corner_edge<4:
        # Check for corner tile
            if (edge_sums[i][0] == 0 and edge_sums[i][1] == 0 and edge_sums[i][2] != 0 and edge_sums[i][3] != 0):
                pos_array[0]=i
                edge_sums[i][4]=True
                corner_edge+=1
            if (edge_sums[i][0] != 0 and edge_sums[i][1] == 0 and edge_sums[i][2] == 0 and edge_sums[i][3] != 0):
                pos_array[39]=i
                edge_sums[i][4]=True
                corner_edge+=1
            if (edge_sums[i][0] != 0 and edge_sums[i][1] != 0 and edge_sums[i][2] == 0 and edge_sums[i][3] == 0):
                pos_array[1999]=i
                edge_sums[i][4]=True
                corner_edge+=1
            if (edge_sums[i][0] == 0 and edge_sums[i][1] != 0 and edge_sums[i][2] != 0 and edge_sums[i][3] == 0):
                pos_array[1960]=i
                edge_sums[i][4]=True
                corner_edge+=1
        else :
            print("corner tiles are placed in mosaic!")
            break

# left edge of the mosaic
count1=40
for i in range(0, 1200):
    
    if edge_sums[i][4] == False :
        # left edge of the mosaic
        if edge_sums[i][0] == 0:
            # place on the left edge but not in correct position
            pos_array[count1]=i
            count1+=40# move to next row
    if count1==1960:
        print("place on the left edge but not in correct position!")
        break

sorted=False
count=0 # first element on the left edge in correct position
best_pos=40
while (sorted==False):
    sorted=True
    # swapped=False
    count1=count+80
    while (count<1920):
        diff1=abs(edge_sums[pos_array[count]][3]-edge_sums[pos_array[best_pos]][1])
        diff2=abs(edge_sums[pos_array[count]][3]-edge_sums[pos_array[count1]][1])
        if diff1>diff2:
            best_pos=count1
            sorted=False
        count1+=40

                




for i in range(1, 1201):
    # Open the image file
    img = Image.open(f'images/({pos_array(i)}).png')
    # Calculate the position in the mosaic where this image will be placed
    pos = ((i-1)%image_size[0]*tile_size[0], (i-1)//image_size[0]*tile_size[1])
    # Paste the current image into the mosaic
    mosaic.paste(img, pos)



# Save the mosaic image in the 'png_combined/' directory
os.makedirs('png_combined', exist_ok=True)
mosaic.save('png_combined/mosaic1.png')

# print(edge_sums)
# Open the file in write mode ('w')
with open('output_sum.txt', 'w') as f:
    # Write each item from the data list to the file
    for item in edge_sums:
        f.write(str(item) + "\n")