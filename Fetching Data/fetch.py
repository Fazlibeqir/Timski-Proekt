import requests
import os
import magic  # This library helps to identify file types
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
import mimetypes

# Define the dataset key and the output directory
dataset_key = "03f2256a-e548-43d7-a731-253302f4aa34"
output_dir = "images"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# GBIF API URL for occurrences with media
api_url = f"https://api.gbif.org/v1/occurrence/search?datasetKey={dataset_key}&mediaType=StillImage&limit=1000"

# Fetch the occurrence records
response = requests.get(api_url)
data = response.json()

mime = magic.Magic(mime=True)

def download_image(record, i, j, media):
    scientific_name = record.get('scientificName', 'Unknown').replace(' ', '_')
    image_url = media['identifier']
    img_data = requests.get(image_url).content

    file_type = mime.from_buffer(img_data)

    if 'image' in file_type:
        extension = file_type.split('/')[-1]
        image_name = os.path.join(output_dir, f"{scientific_name}_{i}_{j}.{extension}")
        with open(image_name, 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded {image_name} (Scientific Name: {scientific_name})")
    else:
        print(f"Skipped non-image file: {image_url}")

# Download images concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for i, record in enumerate(data['results']):
        if 'media' in record:
            for j, media in enumerate(record['media']):
                if media.get('type') == 'StillImage':
                    scientific_name = record.get('scientificName', 'Unknown').replace(' ', '_')
                    extension = media['identifier'].split('.')[-1]
                    image_name = os.path.join(output_dir, f"{scientific_name}_{i}_{j}.{extension}")
                    if os.path.exists(image_name):
                        print(f"Exists: {image_name}")
                    else:
                        futures.append(executor.submit(download_image, record, i, j, media))

print("Download complete.")

stats = defaultdict(lambda: defaultdict(int))

for root, dirs, files in os.walk(output_dir):
    for file in files:
        if file.endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')):
            scientific_name = '_'.join(file.split('_')[:-2])
            file_type = mimetypes.guess_type(file)[0]
            stats[scientific_name]['count'] += 1
            stats[scientific_name][file_type] += 1

print("\nStatistics:")
for scientific_name, data in stats.items():
    print(f"\nScientific Name: {scientific_name}")
    print(f"Total Images: {data['count']}")
    for file_type, count in data.items():
        if file_type != 'count':
            print(f"{file_type}: {count}")