import FramesToVideo
import FrameCreation

path = 'Dishonoured.jpg'

print("Encoding data...")

FrameCreation.createFrames(path)
FramesToVideo.createVideo()

print("Data encoded successfully.")
