import sys
import FramesToVideo
import FrameCreation

if len(sys.argv) < 2:
    print("Please provide the path as a command-line argument.")
    sys.exit(1)

path = sys.argv[1]

print("Encoding data...")

FrameCreation.createFrames(path)
FramesToVideo.createVideo()

print("Data encoded successfully.")
