import cv2
import os
import glob
from tqdm import tqdm

def change_fps_and_resolution(src_path, dst_path, new_fps, new_width, new_height):
    cap = cv2.VideoCapture(src_path)

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    frame_interval = round(fps / new_fps)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(dst_path, fourcc, new_fps, (new_width, new_height))

    frame_id = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % frame_interval == 0:
            frame = cv2.resize(frame, (new_width, new_height))
            out.write(frame)

        frame_id += 1

    cap.release()
    out.release()

source_path = "/source_path"
destination_path = "/output_path"
files = glob.glob(os.path.join(source_path, "*.mp4"))

for file in tqdm(files, desc="Processing videos"):
    filename = os.path.basename(file)
    dst_path = os.path.join(destination_path, filename)
    change_fps_and_resolution(file, dst_path, 25, 256, 256)
