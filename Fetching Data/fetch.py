import requests
import os
import magic  # This library helps to identify file types

# Define the dataset key and the output directory
dataset_key = "03f2256a-e548-43d7-a731-253302f4aa34"
output_dir = "gbif_images"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# GBIF API URL for occurrences with media
api_url = f"https://api.gbif.org/v1/occurrence/search?datasetKey={dataset_key}&mediaType=StillImage&limit=1000"

# Fetch the occurrence records
response = requests.get(api_url)
data = response.json()

# Initialize the magic library
mime = magic.Magic(mime=True)

# Download images
for record in data['results']:
    if 'media' in record:
        for i, media in enumerate(record['media']):
            if media['type'] == 'StillImage':
                image_url = media['identifier']
                image_name = os.path.join(output_dir, os.path.basename(image_url))
                img_data = requests.get(image_url).content
                
                # Identify the file type
                file_type = mime.from_buffer(img_data)
                
                # Save the file with the correct extension
                if 'image' in file_type:
                    extension = file_type.split('/')[-1]
                    image_name = f"{os.path.splitext(image_name)[0]}_{i}.{extension}"
                    with open(image_name, 'wb') as handler:
                        handler.write(img_data)
                    print(f"Downloaded {image_name}")
                else:
                    print(f"Skipped non-image file: {image_url}")

print("Download complete.")