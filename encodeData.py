import FramesToVideo
import FrameCreation

path = 'ENTER_YOUR_FILE_PATH'

print("Encoding data...")

FrameCreation.createFrames(path)
FramesToVideo.createVideo()

print("Data encoded successfully.")
