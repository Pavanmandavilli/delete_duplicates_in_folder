import os
import imagehash
from PIL import Image

folder_path = 'F:\masks'  # Replace with the path to your folder

# Create a dictionary to store image hashes and their corresponding file paths
hashes = {}

# Function to compute the hash of an image
def compute_hash(file_path):
    with Image.open(file_path) as img:
        hash_value = imagehash.average_hash(img)
    return str(hash_value)

# Iterate through the files in the folder and identify duplicates
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is an image (you can add more image extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_hash = compute_hash(file_path)
        
        # Check if the hash already exists (duplicate image)
        if image_hash in hashes:
            print(f"Removing duplicate: {filename}")
            os.remove(file_path)
        else:
            hashes[image_hash] = file_path

print("Duplicate images removed successfully.")
