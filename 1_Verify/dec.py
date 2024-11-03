import os
import hashlib

target_checksum = 'b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2'

def calculate_sha256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

matching_file = None

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        checksum = calculate_sha256(filename)
        if checksum == target_checksum:
            matching_file = filename
            print(f'Matching file: {filename}')

# Remove all files except the matching file and this script
for filename in os.listdir('.'):
    if os.path.isfile(filename) and filename != matching_file and filename != os.path.basename(__file__):
        os.remove(filename)
        print(f'Removed file: {filename}')
