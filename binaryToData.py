import base64
import os
import pickle
from pathlib import Path


def getData():

    print("Extracting data...")

    with open("binary.txt", "r") as f:
        binary_string = f.read()

    hex_string = '%0*X' % ((len(binary_string) + 3) // 4, int(binary_string, 2))

    # Convert the hexadecimal string to binary data
    binary_data = bytes.fromhex(hex_string)

    decoded_data = pickle.loads(base64.b64decode(binary_data))

    original_data = decoded_data["data"]
    name = decoded_data["metadata"]["name"]
    file_format = decoded_data["metadata"]["format"]

    output_file_path = Path(f"{name}.{file_format}")
    with output_file_path.open('wb') as new_file:
        new_file.write(original_data)

    os.remove("binary.txt")

    print("File reconstructed successfully.")
