import shutil

import cv2
import os


# Input directory containing frames

def createVideo():

    print("Creating video...")

    input_directory = 'Frames'
    output_video_filename = 'output_video.avi'

    frame_files = sorted([os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.bmp')])

    if not frame_files:
        print("No frame files found.")
        return

    # Read the dimensions of the first frame
    first_frame = cv2.imread(frame_files[0])
    frame_height, frame_width, _ = first_frame.shape

    # Initialize the VideoWriter object with FFV1 codec
    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    out = cv2.VideoWriter(output_video_filename, fourcc, 30.0, (frame_width, frame_height))

    # Loop through the frame files and add each frame to the video
    for frame_file in frame_files:
        frame = cv2.imread(frame_file)
        out.write(frame)

    # Release the VideoWriter
    out.release()

    # Clean up the 'Frames' directory
    shutil.rmtree(input_directory)

    print(f"Video '{output_video_filename}' created successfully.")
