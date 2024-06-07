import os
import cv2
import pyautogui
import uvicorn
from PIL import ImageGrab
from easyocr import Reader
from fastapi import FastAPI
from ultralytics import YOLOv10

app = FastAPI()
cap = cv2.VideoCapture(0)  # 初始化摄像头
model = YOLOv10("model/yolov10m.pt")  # 加载YOLOv10模型,确保模型权重文件路径正确
object_count = {}  # 创建一个空字典用于统计物品个数
name_map = {"0": "个人", "1": "辆自行车", "2": "辆汽车", "3": "辆摩托车", "4": "架飞机", "5": "辆公共汽车",
            "6": "列火车", "7": "辆卡车", "8": "艘船", "9": "个交通灯", "10": "个消防栓", "11": "个停车标志",
            "12": "个停车计时器", "13": "张长椅", "14": "只鸟", "15": "只猫", "16": "只狗", "17": "匹马",
            "18": "只绵羊", "19": "头奶牛", "20": "头大象", "21": "只熊", "22": "只斑马", "23": "只长颈鹿",
            "24": "个背包", "25": "把伞", "26": "个手提包", "27": "条领带", "28": "个行李箱", "29": "个飞盘",
            "30": "副滑雪板", "31": "块滑雪板", "32": "个运动球", "33": "个风筝", "34": "根棒球棒",
            "35": "个棒球手套", "36": "块滑板", "37": "块冲浪板", "38": "个网球拍", "39": "个瓶子", "40": "个酒杯",
            "41": "个杯子", "42": "把叉子", "43": "把刀子", "44": "把勺子", "45": "个碗", "46": "根香蕉",
            "47": "个苹果", "48": "个三明治", "49": "个橙子", "50": "棵西兰花", "51": "根胡萝卜", "52": "个热狗",
            "53": "张比萨", "54": "个甜甜圈", "55": "块蛋糕", "56": "把椅子", "57": "张沙发", "58": "盆盆栽",
            "59": "张床", "60": "张餐桌", "61": "个厕所", "62": "台显示器", "63": "台笔记本电脑", "64": "个鼠标",
            "65": "个遥控器", "66": "个键盘", "67": "部手机", "68": "台微波炉", "69": "台烤箱", "70": "个烤面包机",
            "71": "个水槽", "72": "台冰箱", "73": "本书", "74": "个时钟", "75": "个花瓶", "76": "把剪刀",
            "77": "个泰迪熊", "78": "个吹风机", "79": "把牙刷"}


def yolo_camera():
    global object_count
    ret, frame = cap.read()  # 读取一帧
    results = model(frame)[0]  # YOLOv10检测
    names = results.names  # 获取检测到的物体名称
    detected_objects = []  # 创建一个空列表来存储检测到的物体名称
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = box.cls.item()
            name = names[int(cls)]
            if name in name_map:
                name = name_map[name]
                detected_objects.append(name)
                object_count[name] = object_count.get(name, 0) + 1  # 统计物品个数
    count_output = '、'.join([f'{count}{name}' for name, count in object_count.items()])  # 输出规范化统计结果
    object_count = {}  # 清零计数
    return count_output


def yolo_screen():
    global object_count
    width, height = pyautogui.size()  # 使用pyautogui来获取屏幕大小
    screenshot = ImageGrab.grab(bbox=(0, 0, width, height))  # 截图整个屏幕
    screenshot.save("cache.jpg", "JPEG")  # 保存截图到文件
    results = model("cache.jpg")[0]  # YOLOv10检测
    names = results.names  # 获取检测到的物体名称
    detected_objects = []  # 创建一个空列表来存储检测到的物体名称
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = box.cls.item()
            name = names[int(cls)]
            if name in name_map:
                name = name_map[name]
                detected_objects.append(name)
                object_count[name] = object_count.get(name, 0) + 1  # 统计物品个数
    count_output = '、'.join([f'{count}{name}' for name, count in object_count.items()])  # 输出规范化统计结果
    object_count = {}  # 清零计数
    os.remove("cache.jpg")
    return count_output


def ocr_screen():
    text = ""
    width, height = pyautogui.size()  # 使用pyautogui来获取屏幕大小
    screenshot = ImageGrab.grab(bbox=(0, 0, width, height))  # 截图整个屏幕
    screenshot.save("cache.jpg", "JPEG")  # 保存截图到文件
    reader = Reader(['ch_sim', 'en'], model_storage_directory="model")  # 使用EasyOCR进行OCR识别
    result = reader.readtext("cache.jpg")
    temp_text = ""  # 初始化一个临时字符串用于存储本次识别的文本
    for bbox, ocr_text, prob in result:  # 遍历识别结果
        if prob >= 0.50:  # 只考虑概率大于等于75%的结果
            temp_text += ocr_text + " "  # 将识别到的文本追加到临时字符串，并加上空格分隔
    text += temp_text + " "  # 将本次识别的文本追加到全局 text 变量中，并加上换行符分隔
    os.remove("cache.jpg")
    return text


@app.get("/yolo")  # 使用举例：http://127.0.0.1:8089/yolo
async def get_yolocam_result():
    answer = yolo_camera()
    return {"answer": answer}


@app.get("/yoloscreen")  # 使用举例：http://127.0.0.1:8089/yoloscreen
async def get_yoloscreen_result():
    answer = yolo_screen()
    return {"answer": answer}


@app.get("/ocr")  # 使用举例：http://127.0.0.1:8089/ocr
async def get_ocr_result():
    answer = ocr_screen()
    return {"answer": answer}


print("本地图像识别模型API服务器启动成功!")
uvicorn.run(app, host="0.0.0.0", port=8089)
