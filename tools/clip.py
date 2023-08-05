import json
import os
import pandas as pd
import subprocess

# 读取json文件
with open("NurViD_annotations.json", "r") as f:
    data = json.load(f)

# 创建一个空的列表，用于存储剪辑视频的信息
video_info = []

# 遍历json文件中的每个视频
video_names = data.keys()
for video_name in video_names:
    video_path = data[video_name]["url"]
    video_name = video_path.split("=")[-1]

    # 指定本地视频所在的目录
    video_dir = "/video_path"

    # 拼接本地视频的完整路径
    video_path = os.path.join(video_dir, video_name+'.mp4')

    operation_id = data[video_name]["procedureID"]
    annotations = data[video_name]["annotations"]


    # 遍历每个视频的标注片段
    for i, annotation in enumerate(annotations):
        action_id = annotation["actionID"]
        start_time = annotation["segment"][0]
        end_time = annotation["segment"][1]
        duration = end_time - start_time

        # 指定导出视频所在的目录
        new_video_dir = "/segments_save_path"

        # 拼接导出视频的完整路径
        new_video_name = os.path.join(new_video_dir, video_name + "_" + str(i + 1) + ".mp4")

        # 用ffmpeg命令剪辑视频
        command = f"ffmpeg -ss {start_time} -i {video_path} -t {duration} -c copy {new_video_name}"
        #subprocess.call(command)
        os.system(command)

        # 将剪辑视频的信息作为一个字典添加到列表中
        video_info.append({"Video Name": new_video_name, "Operation ID": operation_id, "Action ID": action_id})

# 将列表转换为DataFrame对象
df = pd.DataFrame(video_info)

# 将DataFrame对象保存为excel文件，文件名为视频名字加.xlsx
output_file = "excel_save_path"
df.to_excel(output_file, index=False)
