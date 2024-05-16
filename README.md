# yolo_ocr_api_server
YOLOv8&amp;EasyOCR融合图像识别API服务器

本项目整合了ultralytics开发的YOLOv8图像物品识别模型和JaidedAI开发的EasyOCR图像文字识别模型，提供快速、准确的图像识别服务。

## 项目源地址
- YOLOv8: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
- EasyOCR: [https://github.com/JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR)

## 安装依赖
   ```
   pip install -r requirements.txt
   ```

## 运行方式
python img_api_server.py

## 服务器地址
图像识别模型API服务器地址默认为：`http://你的电脑IP:8089/`

## API接口
### 图像物品识别模型
- **接口地址**: `/yolo/`
- **请求方式**: `GET`
- **请求参数**: 无

### 图像文字识别模型
- **接口地址**: `/ocr/`
- **请求方式**: `GET`
- **请求参数**: 无

## 使用示例
### 图像物品识别
1. 在浏览器地址栏输入以下地址：
   ```
   http://127.0.0.1:8089/yolo/
   ```
2. 按下回车键，服务器将返回JSON格式的识别结果，例如：
   ```json
   {"answer":"1台显示器、1个人"}
   ```

### 图像文字识别
1. 在浏览器地址栏输入以下地址：
   ```
   http://127.0.0.1:8089/ocr/
   ```
2. 按下回车键，服务器将返回JSON格式的识别结果，例如：
   ```json
   {"answer":"屏幕识别结果"}
   ```

## 注意事项
1. 运行API服务器前需确保电脑摄像头已连接。
2. API服务器仅支持`GET`请求方式。
3. 服务器返回的图像识别结果仅供参考，如有不准确之处，请以实际场景为准。

## 贡献与反馈
欢迎对本项目提出改进意见或贡献代码。

## 许可证
本项目采用MIT开源协议，详情请查看[LICENSE](LICENSE)文件。
