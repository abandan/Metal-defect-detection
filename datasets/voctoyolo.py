import xml.etree.ElementTree as ET
import os
import glob


def convert_voc_to_yolo(xml_dir, output_dir):
    # 遍历目录下所有XML文件
    xml_files = glob.glob(os.path.join(xml_dir, '*.xml'))

    for xml_file in xml_files:
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # 提取图像尺寸
            size = root.find('size')
            width = int(size.find('width').text)
            height = int(size.find('height').text)

            # 构建输出路径
            txt_name = os.path.splitext(os.path.basename(xml_file))[0] + '.txt'
            txt_path = os.path.join(output_dir, txt_name)

            with open(txt_path, 'w') as f:
                for obj in root.findall('object'):
                    class_name = obj.find('name').text
                    class_id = int(class_name.split('_')[0])  # 假设类别名为"数字_描述"

                    bbox = obj.find('bndbox')
                    xmin = int(bbox.find('xmin').text)
                    ymin = int(bbox.find('ymin').text)
                    xmax = int(bbox.find('xmax').text)
                    ymax = int(bbox.find('ymax').text)

                    # 计算归一化坐标
                    x_center = (xmin + xmax) / 2.0 / width
                    y_center = (ymin + ymax) / 2.0 / height
                    w = (xmax - xmin) / width
                    h = (ymax - ymin) / height

                    f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

            print(f"转换完成: {os.path.basename(xml_file)} -> {txt_name}")

        except Exception as e:
            print(f"错误：处理文件 {xml_file} 时发生异常 - {str(e)}")


if __name__ == "__main__":
    xml_directory = r"C:\Users\PC\Desktop\voc"  # 包含XML文件的目录
    output_directory = r"C:\Users\PC\Desktop\YOLO\labels"  # 输出目录
    os.makedirs(output_directory, exist_ok=True)
    convert_voc_to_yolo(xml_directory, output_directory)