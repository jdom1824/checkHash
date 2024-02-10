## Hashing and Checker Integrity for CONEXALAB
## Author jdom1824@inaoep.mx

This script is designed to calculate hashes of files in a directory and verify their integrity, ensuring that files have not been tampered with. It also provides a summary of the process, including the total number of files processed and any encountered errors.

## Installation

Recommend you have Python 3.11.7 installed on your system. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/jdom1824/checkHash.git
cd checkHash
```
1. **Install Dependencies:**
You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

2. **How to Use printerHash.py**

This script calculates hashes of files in a directory and saves the results to a JSON file. Follow the steps below to use the script effectively:

Execute the printerHash.py script by running the following command:
```bash
python3 printerHash.py
```
* Enter the Directory Path:

    When prompted, enter the full path to the directory containing the files you want to calculate hashes for and press Enter.

* Monitor Progress:

    The script will start calculating hashes for the files in the specified directory. You'll see a progress bar indicating the status of each file's hash calculation.

* View Results:

    Once the script completes the hash calculation process, it will save the results to a JSON file named <directory_name>_hashes.json in the same directory.

3. **How to Use checkHash.py**