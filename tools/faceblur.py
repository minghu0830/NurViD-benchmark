import os
import cv2
import concurrent.futures
from tqdm import tqdm

def blur_faces_in_video(video_path, output_path):
    # 加载人脸识别器（这里使用OpenCV的Haar级联分类器）
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建视频编写器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        # 读取视频帧
        ret, frame = video.read()

        if not ret:
            break

        # 将帧转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 对每个检测到的人脸进行模糊处理
        for (x, y, w, h) in faces:
            # 提取人脸区域
            face_roi = frame[y:y+h, x:x+w]

            # 应用模糊处理
            blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)

            # 将模糊后的人脸区域放回原始帧
            frame[y:y+h, x:x+w] = blurred_face

        # 将处理后的帧写入输出视频
        output_video.write(frame)

    # 释放资源
    video.release()
    output_video.release()

def process_video(video):
    input_path, output_path = video
    blur_faces_in_video(input_path, output_path)

def blur_faces_in_videos(input_folder, output_folder):
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 构建视频文件路径列表
    videos = []
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.mp4'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            videos.append((input_path, output_path))

    # 使用多线程处理视频
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_video, video) for video in videos]

        # 显示进度条
        for _ in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc='Processing Videos'):
            pass

    print("批量处理完成！")

# 使用示例
input_folder_path = "input_folder"
output_folder_path = "output_folder"

blur_faces_in_videos(input_folder_path, output_folder_path)