import FramesToVideo
import FrameCreation

path = 'Sound.mp3'

print("Encoding data...")

FrameCreation.createFrames(path)
FramesToVideo.createVideo()

print("Data encoded successfully.")
