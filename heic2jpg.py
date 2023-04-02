import os
from PIL import Image

# Set the current folder as input folder
input_folder = os.getcwd()

# Create a target folder "JPG" in the current folder if it doesn't exist
output_folder = os.path.join(os.getcwd(), 'JPG')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a .heic file
    if filename.lower().endswith(('.heic', '.heic')):
        # Open the image and convert it to .jpg format
        try:
            with Image.open(os.path.join(input_folder, filename)) as img:
                img.convert('RGB').save(os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg'))
                print(f"{filename} was successfully converted to .jpg.")
        except Exception as e:
            print(f"Error converting {filename} to .jpg: {e}")
