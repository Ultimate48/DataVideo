import FramesToVideo
import FrameCreation

path = 'Edited Photos.zip'

print("Encoding data...")

FrameCreation.createFrames(path)
FramesToVideo.createVideo()

print("Data encoded successfully.")
