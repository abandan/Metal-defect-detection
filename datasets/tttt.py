# coding=utf-8

import os
import shutil
import random

# 源文件夹路径
source_dir = r'C:\Users\PC\Desktop\YOLO\img'
# 目标文件夹路径
target_dirs = [
    r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\train\images',
    r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\valid\images',
    r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\test\images'
]

# 确保目标文件夹存在
for dir_path in target_dirs:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# 获取源文件夹中所有图片文件
images = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# 分配比例
train_ratio = 8
valid_ratio = 1
test_ratio = 1
total_ratio = train_ratio + valid_ratio + test_ratio

# 分配图片
for image in images:
    # 随机生成一个介于0和total_ratio之间的数
    ratio = random.randint(0, total_ratio - 1)

    # 根据比例分配到不同的文件夹
    if ratio < train_ratio:
        target_dir = target_dirs[0]
    elif ratio < train_ratio + valid_ratio:
        target_dir = target_dirs[1]
    else:
        target_dir = target_dirs[2]

    # 构建完整的源文件和目标文件路径
    source_image = os.path.join(source_dir, image)
    target_image = os.path.join(target_dir, image)

    # 复制文件
    shutil.copy2(source_image, target_image)
