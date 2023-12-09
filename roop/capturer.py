from typing import Optional
import cv2
import numpy as np
from PIL import Image

from roop.typing import Frame

def get_image_frame(filename: str):
    try:
        if isinstance(filename, Image.Image):
            frame = cv2.cvtColor(np.array(filename), cv2.COLOR_RGB2BGR)
        else:
            frame = cv2.imread(filename)
        return frame
    except:
        print(f"Exception reading {filename}")
    return None
    
def get_video_frame(video_path: str, frame_number: int = 0) -> Optional[Frame]:
    capture = cv2.VideoCapture(video_path)
    frame_total = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    capture.set(cv2.CAP_PROP_POS_FRAMES, min(frame_total, frame_number - 1))
    has_frame, frame = capture.read()
    capture.release()
    if has_frame:
        return frame
    return None


def get_video_frame_total(video_path: str) -> int:
    capture = cv2.VideoCapture(video_path)
    video_frame_total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()
    return video_frame_total
