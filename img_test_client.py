import requests


def get_result(choice):
    url = f"http://127.0.0.1:8089/{choice}"
    # 发送请求
    response = requests.get(url)
    # 解析JSON响应
    response_json = response.json()
    # 返回图像识别模型的识别结果
    return response_json["answer"]


while True:
    user_input = input("输入y按下回车进行YOLO摄像头画面识别测试，输入o后按下回车进行OCR屏幕识别测试:")
    if user_input == "y":
        print("请求发送成功，等待YOLO摄像头画面识别...")
        try:
            yolo_response = get_result("yolo")
            print(f"YOLO摄像头画面识别结果: {yolo_response}")
        except:
            print("提示: 图像识别模型API服务器未开启或摄像头未连接。")
    elif user_input == "o":
        print("请求发送成功，等待OCR屏幕识别...")
        try:
            ocr_response = get_result("ocr")
            print(f"OCR屏幕识别结果: {ocr_response}")
        except:
            print("提示: 图像识别模型API服务器未开启或摄像头未连接。")
