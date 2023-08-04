# NurViD: A Large Expert-Level Video Database for Nursing Procedure Activity Understanding
[Ming Hu](https://minghu0830.github.io/), [Lin Wang](https://wanglin-research.com/), [Siyuan Yan](https://github.com/SiyuanYan1), [Don Ma](), [Qingli Ren](), [Peng Xia](https://peng-xia.site/), [Wei Feng](https://fengweie.github.io/), [Peibo Duan](https://scholar.google.com/citations?user=wdIMVqsAAAAJ&hl=zh-CN), [Lie Ju](), [Zongyuan Ge](https://zongyuange.github.io/).

<a href=''><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a>

## Introduction
NurViD is a large video dataset with expert-level annotation for nursing procedure activity understanding. NurViD consists of over 1.5k videos totaling 144 hours. Notably, it encompasses 51 distinct nursing procedures and 177 action steps.

![demo](./localization.png)

## Environment Requirements
1. python=3.8
2. PyTorch 1.8+
3. densflow
4. mmaction2

## Dataset Preparation

### 1.Download videos
Download videos automatically from the source YouTube by running the script below：
```
python /tools/download_videos.py
```
### 2.Preprocess videos
By running the script below, the video will be resized to the short edge size of 256 and a frame rate of 25 FPS:
```
python /tools/preprocess_videos.py
```
### 3.Extract RGB and Flow features
We start by extracting frames from each video at 25 frames per second and optical flow using the TV-L1 algorithm.:
```
python /feature_extraction/build_rawframes.py /video_path /rgb&flow_frmaes_save_path --level 1 --flow-type tvl1 --ext mp4 --task both
```
Next, we utilize a pre-trained I3D model on the ImageNet dataset to generate features for each RGB and optical flow frame:
```
python /feature_extraction/extract_features.py --mode rgb --load_model models/rgb_imagenet.pt --input_dir /rgb&flow_frmaes_save_path --output_dir /rgb_feature_save_path --batch_size 100 --sample_mode resize --no-usezip
python /feature_extraction/extract_features.py --mode flow --load_model models/flow_imagenet.pt --input_dir /rgb&flow_frmaes_save_path --output_dir /rgb_feature_save_path --batch_size 100 --sample_mode resize --no-usezip
```
To handle varying video durations, we perform uniform interpolation to generate 100 fixed-length features for each video. Lastly, we combine the RGB and optical flow features into a 2048-dimensional embedding as the model input:

```
python /feature_extraction/convert.py
```

### 4.Ours
We also provide a method to directly access our data, but it requires you to sign the [data agreement form](). Once you have completed the form, you will receive an email from our team with a Google Drive download link(including original videos, preprocessed videos and features).

## Dataset and code release progress
- [x] Start release
- [x] Add video and annotation files
- [ ] Add RGB and Flow features
- [ ] Add code
