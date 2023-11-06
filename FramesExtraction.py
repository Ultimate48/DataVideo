import cv2
import os


def extractFrames(video_path):

    print("Extracting frames...")

    os.makedirs('ExtractedFrames', exist_ok=True)

    input_video_filename = video_path

    output_frame_directory = 'ExtractedFrames'

    os.makedirs(output_frame_directory, exist_ok=True)

    cap = cv2.VideoCapture(input_video_filename)

    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        output_frame_filename = os.path.join(output_frame_directory, f'frame_{frame_number:04d}.bmp')
        cv2.imwrite(output_frame_filename, frame)

        frame_number += 1

    cap.release()

    print(f"{frame_number} frames extracted and saved in '{output_frame_directory}'")
