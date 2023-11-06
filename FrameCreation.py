import os

from PIL import Image
from extractBinary import extract_binary


def createFrames(path):
    if not os.path.exists('Frames'):
        os.makedirs('Frames')

    print("Creating frames...")

    binary = extract_binary(path)

    frame_width, frame_height = 160, 90

    pixel_data = []

    for bit in binary:
        if bit == '0':
            r, g, b = 0, 0, 0  # Black
        elif bit == '1':
            r, g, b = 255, 255, 255  # White
        else:
            continue
        pixel_data.append((r, g, b))

    pixel_data.append((255, 0, 0))
    pixel_data.append((0, 255, 0))
    pixel_data.append((0, 0, 255))

    frame_number = 1
    i = 0

    while i < len(pixel_data):
        frame = Image.new('RGB', (frame_width, frame_height))
        for y in range(frame_height):
            for x in range(frame_width):
                if i >= len(pixel_data):
                    break
                frame.putpixel((x, y), pixel_data[i])
                i += 1

        frame.save(f'Frames/output_image{frame_number:04d}.bmp')
        frame_number += 1

    print(f"{frame_number - 1} frames created and saved successfully.")
