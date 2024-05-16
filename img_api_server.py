import os
import cv2
import pyautogui
import uvicorn
from PIL import ImageGrab
from easyocr import Reader
from fastapi import FastAPI
from ultralytics import YOLO

app = FastAPI()
# 初始化摄像头
cap = cv2.VideoCapture(0)
# 加载YOLOv8模型
model = YOLO("model/yolov8m.pt")  # 确保模型权重文件路径正确
# 创建一个空字典用于统计物品个数
object_count = {}
name_map = {"person": "个人", "bicycle": "辆自行车", "car": "辆汽车", "motorcycle": "辆摩托车", "airplane": "架飞机",
            "bus": "辆公共汽车", "train": "列火车", "truck": "辆卡车", "boat": "艘船", "traffic light": "个交通灯",
            "fire hydrant": "个消防栓", "stop sign": "个停车标志", "parking meter": "个停车计时器", "bench": "张长椅",
            "bird": "只鸟", "cat": "只猫", "dog": "只狗", "horse": "匹马", "sheep": "只绵羊", "cow": "头奶牛",
            "bowl": "个碗", "elephant": "头大象", "bear": "只熊", "zebra": "只斑马", "giraffe": "只长颈鹿",
            "backpack": "个背包", "umbrella": "把伞", "handbag": "个手提包", "tie": "条领带", "suitcase": "个行李箱",
            "frisbee": "个飞盘", "skis": "副滑雪板", "snowboard": "块滑雪板", "sports ball": "个运动球",
            "kite": "个风筝",
            "fork": "把叉子", "baseball bat": "根棒球棒", "baseball glove": "个棒球手套", "skateboard": "块滑板",
            "surfboard": "块冲浪板", "tennis racket": "个网球拍", "bottle": "个瓶子", "wine glass": "个酒杯",
            "cup": "个杯子", "knife": "把刀子", "spoon": "把勺子", "banana": "根香蕉", "apple": "个苹果",
            "sandwich": "个三明治", "orange": "个橙子", "broccoli": "棵西兰花", "carrot": "根胡萝卜",
            "hot dog": "个热狗",
            "pizza": "张比萨", "donut": "个甜甜圈", "cake": "块蛋糕", "chair": "把椅子", "couch": "张沙发",
            "potted plant": "盆盆栽", "bed": "张床", "tv": "台显示器", "dining table": "张餐桌", "toilet": "个厕所",
            "laptop": "台笔记本电脑", "mouse": "个鼠标", "remote": "个遥控器", "keyboard": "个键盘",
            "cell phone": "部手机",
            "microwave": "台微波炉", "oven": "台烤箱", "vase": "个花瓶", "sink": "个水槽", "refrigerator": "台冰箱",
            "book": "本书", "clock": "个时钟", "toaster": "个烤面包机", "scissors": "把剪刀", "teddy bear": "个泰迪熊",
            "hair drier": "个吹风机", "toothbrush": "把牙刷"}


def recog_things():
    global object_count
    # 读取一帧
    ret, frame = cap.read()
    # YOLOv8检测
    results = model(frame)[0]
    # 获取检测到的物体名称
    names = results.names
    detected_objects = []  # 创建一个空列表来存储检测到的物体名称
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = box.cls.item()
            name = names[int(cls)]
            if name in name_map:
                name = name_map[name]
                detected_objects.append(name)
                # 统计物品个数
                object_count[name] = object_count.get(name, 0) + 1
    # 输出规范化统计结果
    count_output = '、'.join([f'{count}{name}' for name, count in object_count.items()])
    object_count = {}  # 清零计数
    return count_output


def recog_screen():
    text = ""
    # 使用pyautogui来获取屏幕大小
    width, height = pyautogui.size()
    # 截图整个屏幕
    screenshot = ImageGrab.grab(bbox=(0, 0, width, height))
    # 保存截图到文件
    screenshot.save("cache.jpg", "JPEG")
    # 使用EasyOCR进行OCR识别
    reader = Reader(['ch_sim', 'en'], model_storage_directory="model")
    result = reader.readtext("cache.jpg")
    # 初始化一个临时字符串用于存储本次识别的文本
    temp_text = ""
    # 遍历识别结果
    for bbox, ocr_text, prob in result:
        if prob >= 0.75:  # 只考虑概率大于等于75%的结果
            temp_text += ocr_text + " "  # 将识别到的文本追加到临时字符串，并加上空格分隔
    # 将本次识别的文本追加到全局 text 变量中，并加上换行符分隔
    text += temp_text + " "
    os.remove("cache.jpg")
    return text


@app.get("/yolo")  # 使用举例：http://127.0.0.1:8089/yolo
async def get_yolo_result():
    answer = recog_things()
    return {"answer": answer}


@app.get("/ocr")  # 使用举例：http://127.0.0.1:8089/ocr
async def get_ocr_result():
    answer = recog_screen()
    return {"answer": answer}


print("本地图像识别模型api服务器启动成功!")
uvicorn.run(app, host="0.0.0.0", port=8089)
