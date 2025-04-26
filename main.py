import torch
print(torch.cuda.is_available())
print(torch.backends.cudnn.is_available())
print(torch.version.cuda)
print(torch.backends.cudnn.version())

model = YOLO(abs_path('./weights/yolov8s.pt'), task='detect')  # 加载预训练的YOLOv8模型
results2 = model.train(  # 开始训练模型
    data=data_path,  # 指定训练数据的配置文件路径
    device=device,  # 自动选择进行训练
    workers=workers,  # 指定使用2个工作进程加载数据
    imgsz=640,  # 指定输入图像的大小为640x640
    epochs=300,  # 指定训练150个epoch
    batch=batch,  # 指定每个批次的大小为8
    name='train_v8_' + data_name  # 指定训练任务的名称
)