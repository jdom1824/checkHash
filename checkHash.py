import hashlib
import os
import json
import time
from colorama import Fore, Style

def calculate_hash(file_path, algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.

    :param file_path: Path of the file.
    :param algorithm: Hash algorithm to use (default: 'sha256').
    :return: The calculated hash in hexadecimal format.
    """
    if algorithm.lower() == 'sha1':
        hash_func = hashlib.sha1()
    elif algorithm.lower() == 'sha256':
        hash_func = hashlib.sha256()
    elif algorithm.lower() == 'md5':
        hash_func = hashlib.md5()
    else:
        raise ValueError("Invalid hash algorithm")

    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b''):
            hash_func.update(block)

    return hash_func.hexdigest()

def verify_hashes(directory_path, json_file):
    """
    Verify hashes of files in the directory with the hashes from the JSON file.

    :param directory_path: Path of the directory containing the files.
    :param json_file: Path of the JSON file containing the hashes.
    """
    # Load hashes from JSON file
    with open(json_file, 'r') as f:
        expected_hashes = json.load(f)
    # Initialize counters
    matching_files = 0
    mismatching_files = 0

    # Verify hashes of files in the directory
    for filename, expected_hash in expected_hashes.items():
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            calculated_hash = calculate_hash(file_path)
            if calculated_hash == expected_hash:
                print(f"Hash of file '{filename}' {Fore.GREEN}matches the expected hash.{Style.RESET_ALL}")
                matching_files += 1
            else:
                print(f"Hash of file '{filename}' {Fore.RED}does not match the expected hash.{Style.RESET_ALL}")
                mismatching_files += 1
            time.sleep(0.5)  # Add a delay of 0.5 seconds

    # Print summary
    print(f"\nSummary:")
    print(f"Matching files: {Fore.GREEN}{matching_files}{Style.RESET_ALL}")
    print(f"Mismatching files: {Fore.RED}{mismatching_files}{Style.RESET_ALL}")

# Example usage
directory_path = input("Enter the directory path: ")
json_file = input("Enter the path of the JSON file: ")

verify_hashes(directory_path, json_file)
