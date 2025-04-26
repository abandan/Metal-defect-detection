# coding=utf-8

import os
import shutil

# 定义源文件夹和目标文件夹路径
txt_source_dir = r'C:\Users\PC\Desktop\YOLO\labels'
image_dirs = {
    'train': r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\train\images',
    'valid': r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\valid\images',
    'test': r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\test\images'
}
label_dirs = {
    'train': r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\train\labels',
    'valid': r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\valid\labels',
    'test': r'C:\Users\PC\Desktop\基于YOLOv8和YOLOv5的工业金属表面缺陷检测系统\MetalDefects\datasets\MetalDefects\test\labels'
}

# 确保目标文件夹存在
for dir_path in label_dirs.values():
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# 遍历txt文件
for txt_file in os.listdir(txt_source_dir):
    txt_file_path = os.path.join(txt_source_dir, txt_file)

    # 检查文件扩展名是否为.txt
    if txt_file.endswith('.txt'):
        # 获取不带扩展名的文件名
        base_name = os.path.splitext(txt_file)[0]

        # 遍历所有图片目录
        for label, image_dir in image_dirs.items():
            image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
            if base_name + '.jpg' in image_files or base_name + '.png' in image_files:
                # 找到匹配的图片，移动txt文件到对应的标签文件夹
                target_dir = label_dirs[label]
                target_file_path = os.path.join(target_dir, txt_file)

                # 如果目标文件夹中已经存在同名的txt文件，则跳过
                if os.path.exists(target_file_path):
                    print(f"Skipping {txt_file}, already exists in {target_dir}")
                    continue

                # 移动文件
                shutil.move(txt_file_path, target_file_path)
                print(f"Moved {txt_file} to {target_dir}")
                break  # 找到匹配后跳出循环