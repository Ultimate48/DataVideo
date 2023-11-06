import FramesExtraction
import FrameToBinary
import binaryToData

video_path = 'output_video.avi'


def decodeData():
    print("Decoding data...")

    FramesExtraction.extractFrames(video_path)
    FrameToBinary.getBinary()
    binaryToData.getData()

    print("Data decoded successfully.")


decodeData()
