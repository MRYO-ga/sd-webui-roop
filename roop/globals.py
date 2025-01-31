# from ..scripts import settings
from typing import List

source_path = None
target_path = None
output_path = None
target_folder_path = None

frame_processors: List[str] = []
keep_fps = None
keep_frames = None
skip_audio = None
many_faces = None
use_batch = None
source_face_index = 0
target_face_index = 0
face_position = None
video_encoder = None
video_quality = None
max_memory = None
execution_providers: List[str] = []
execution_threads = None
headless = True
log_level = 'error'
selected_enhancer = "GFPGAN"
face_swap_mode = "selected"
blend_ratio = 0.65
distance_threshold = 0.8
default_det_size = True

processing = False 

FACE_ENHANCER = None

INPUT_FACES = []
TARGET_FACES = []

IMAGE_CHAIN_PROCESSOR = None
VIDEO_CHAIN_PROCESSOR = None
BATCH_IMAGE_CHAIN_PROCESSOR = None

# CFG: Settings = None


