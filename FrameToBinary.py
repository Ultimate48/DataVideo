import shutil

from PIL import Image
import os
import numpy as np

binary = ""


def find_index(pixel_data):
    mask = np.array([255, 255, 255])
    comparison = (pixel_data == mask).all(axis=1)
    index = np.argmax(comparison)
    return index


def decimalToBinary(n):
    return bin(n).replace("0b", "").zfill(8)


def data_save():
    with open("binary.txt", "w") as f:
        f.write(binary)
    print("Data saved to files successfully.")


def extract_binary_from_frames(input_directory):
    global binary
    frame_files = sorted([file for file in os.listdir(input_directory) if file.endswith('.bmp')])

    for frame_file in frame_files:
        frame_path = os.path.join(input_directory, frame_file)
        frame = Image.open(frame_path)
        pixel_data = np.array(frame)

        index = find_index(pixel_data)
        if index != 0:
            pixel_data = pixel_data[:index]

        pixel_data = pixel_data.ravel()
        binary += "".join(map(decimalToBinary, pixel_data))

    data_save()


input_directory = 'ExtractedFrames'


def getBinary():
    print("Extracting binary...")
    extract_binary_from_frames(input_directory)
    shutil.rmtree('ExtractedFrames')
    print("Binary extracted successfully.")
