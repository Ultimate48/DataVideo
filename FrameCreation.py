import os

from PIL import Image
from extractBinary import extract_binary


def binaryToDecimal(binary):
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    return decimal


def createFrames(path):
    if not os.path.exists('Frames'):
        os.makedirs('Frames')

    print("Creating frames...")

    binary = extract_binary(path)
    frame_width, frame_height = 160, 90

    # Convert binary string to decimal integers
    data = [binaryToDecimal(binary[i:i + 8]) for i in range(0, len(binary), 8)]

    # Ensure the data is a multiple of 3 and create groups
    data += [0] * (3 - (len(data) % 3))
    groups = [(data[i], data[i + 1], data[i + 2]) for i in range(0, len(data), 3)]

    # Add color frames
    groups.extend([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

    frame_number = 1
    i = 0

    while i < len(groups):
        frame = Image.new('RGB', (frame_width, frame_height))
        for y in range(frame_height):
            for x in range(frame_width):
                if i >= len(groups):
                    break
                frame.putpixel((x, y), groups[i])
                i += 1

        frame.save(f'Frames/output_image{frame_number:04d}.bmp')
        frame_number += 1

    print(f"{frame_number - 1} frames created and saved successfully.")
