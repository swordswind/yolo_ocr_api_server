import requests


def get_result(choice):
    url = f"http://127.0.0.1:8089/{choice}"
    response = requests.get(url)  # 发送请求
    response_json = response.json()  # 解析JSON响应
    return response_json["answer"]  # 返回图像识别模型的识别结果


while True:
    user_input = input("输入y按下回车进行YOLO摄像头物体识别测试，输入s按下回车进行YOLO屏幕物体识别测试，输入o后按下回车进行OCR屏幕文字识别测试:")
    if user_input == "y":
        print("请求发送成功，等待YOLO摄像头物体识别...")
        try:
            yolocam_response = get_result("yolo")
            print(f"YOLO摄像头物体识别结果: {yolocam_response}\n")
        except:
            print("提示: 图像识别模型API服务器未开启或摄像头未连接。\n")
    elif user_input == "s":
        print("请求发送成功，等待YOLO屏幕物体识别...")
        try:
            yoloscreen_response = get_result("yoloscreen")
            print(f"YOLO屏幕物体识别结果: {yoloscreen_response}\n")
        except:
            print("提示: 图像识别模型API服务器未开启。\n")
    elif user_input == "o":
        print("请求发送成功，等待OCR屏幕文字识别...")
        try:
            ocr_response = get_result("ocr")
            print(f"OCR屏幕文字识别结果: {ocr_response}\n")
        except:
            print("提示: 图像识别模型API服务器未开启。\n")
