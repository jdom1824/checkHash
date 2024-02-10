# Author: jdom1824@inaoep.mx
# This script calculates hashes of files in a directory and saves the results to a JSON file
import hashlib
import os
import json
from tqdm import tqdm
import time

def calculate_hash(file_path, algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.

    :param file_path: Path of the file.
    :param algorithm: Hash algorithm to use (default: 'sha256').
    :return: The calculated hash in hexadecimal format.
    """
    # Select the hash algorithm
    if algorithm.lower() == 'sha1':
        hash_func = hashlib.sha1()
    elif algorithm.lower() == 'sha256':
        hash_func = hashlib.sha256()
    elif algorithm.lower() == 'md5':
        hash_func = hashlib.md5()
    else:
        raise ValueError("Invalid hash algorithm")

    # Calculate the hash of the file
    with open(file_path, 'rb') as f:
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            return hash_func.hexdigest()  # Return an empty hash if the file size is zero

        progress = tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Hashing files {os.path.basename(file_path)}", leave=False, bar_format="{desc:<30} {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]")
        for block in iter(lambda: f.read(4096), b''):
            hash_func.update(block)
            progress.update(len(block))
            time.sleep(0.001)  # Adjust the sleep time as needed
        progress.close()

    # Return the hash in hexadecimal format
    return hash_func.hexdigest()

# Ask the user for the directory path
directory_path = input("Enter the directory path: ")

# Extract directory name
directory_name = os.path.basename(directory_path)

# Dictionary to store file hashes
file_hashes = {}

# Calculate hashes for all files in the directory
for filename in os.listdir(directory_path):
    filepath = os.path.join(directory_path, filename)
    if os.path.isfile(filepath):
        try:
            hash_sha256 = calculate_hash(filepath, algorithm='sha256')
            file_hashes[filename] = hash_sha256
        except Exception as e:
            print(f"Error processing file '{filename}': {e}")

# Write the dictionary of file hashes to a JSON file
output_file = f'{directory_name}_hashes.json'
try:
    with open(output_file, 'w') as f:
        json.dump(file_hashes, f, indent=4)
    print(f"Hashes of files in directory '{directory_path}' have been saved to '{output_file}'")
except Exception as e:
    print(f"Error writing JSON file: {e}")
