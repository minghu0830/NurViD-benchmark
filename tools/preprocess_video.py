import os
import cv2
import threading
from queue import Queue

# Specify the directory to convert
input_dir = "./dataset/original_videos"
# Specify the output directory
output_dir = "./dataset/preprocessed_videos"
# Specify the FPS and resolution for conversion
target_fps = 25
target_width = 256
target_height = 256
# Specify the number of concurrent threads
num_threads = 4

file_queue = Queue()

lock = threading.Lock()

def convert_fps_and_resolution():
    while True:
        file_path = file_queue.get()
        if file_path is None:
            break

        cap = cv2.VideoCapture(file_path)

        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if fps == target_fps and width == target_width and height == target_height:
            lock.acquire()
            os.system(f"cp {file_path} {os.path.join(output_dir, os.path.relpath(file_path, input_dir))}")
            lock.release()
            continue

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        output_path = os.path.join(output_dir, os.path.relpath(file_path, input_dir))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        out = cv2.VideoWriter(output_path, fourcc, target_fps, (target_width, target_height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (target_width, target_height))
            out.write(frame)

        cap.release()
        out.release()

        lock.acquire()
        print(output_path)
        lock.release()

        file_queue.task_done()

for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if not filename.endswith(".mp4"):
            continue

        file_queue.put(os.path.join(root, filename))

threads = []
for i in range(num_threads):
    t = threading.Thread(target=convert_fps_and_resolution)
    t.start()
    threads.append(t)

file_queue.join()

for i in range(num_threads):
    file_queue.put(None)
for t in threads:
    t.join()