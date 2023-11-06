import shutil

import cv2
import os


# Input directory containing frames

def createVideo():

    print("Creating video...")

    input_directory = 'Frames'

    # Output video filename
    output_video_filename = 'output_video.avi'  # Use AVI format for FFV1 codec

    # Get the list of frame filenames in the directory
    frame_files = sorted(
        [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.bmp')])

    # Read the dimensions of the first frame
    frame = cv2.imread(frame_files[0])
    frame_height, frame_width, _ = frame.shape

    # Initialize the VideoWriter object with FFV1 codec
    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    out = cv2.VideoWriter(output_video_filename, fourcc, 120.0, (frame_width, frame_height))

    # Loop through the frame files and add each frame to the video
    for frame_file in frame_files:
        frame = cv2.imread(frame_file)
        out.write(frame)

    # Release the VideoWriter
    out.release()

    shutil.rmtree('Frames')

    print(f"Video '{output_video_filename}' created successfully.")
