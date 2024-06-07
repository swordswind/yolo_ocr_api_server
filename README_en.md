# yolo_ocr_api_server
YOLO10 & EasyOCR Fusion Image Recognition API Server

This project integrates the YOLOv10 image object recognition model developed by THU-MIG and the EasyOCR image text recognition model developed by JaidedAI, providing fast and accurate image recognition services.

## Project Source Address
- YOLOv10: [https://github.com/THU-MIG/yolov10](https://github.com/THU-MIG/yolov10) 
- EasyOCR: [https://github.com/JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR) 

## Installation Dependencies
   ```
   pip install -r requirements.txt
   ```

## Running Method
python img_api_server.py

## Server Address
The default address of the image recognition model API server is: `http://your computer's IP:8089/`

## API Interface
### Camera Object Recognition Model
- **Interface Address**: `/yolo/`
- **Request Method**: `GET`
- **Request Parameters**: None

### Screen Object Recognition Model
- **Interface Address**: `/yoloscreen/`
- **Request Method**: `GET`
- **Request Parameters**: None

### Image Text Recognition Model
- **Interface Address**: `/ocr/`
- **Request Method**: `GET`
- **Request Parameters**: None

## Usage Examples
### Image Object Recognition
1. Enter the following address in the browser's address bar:
   ```
   http://127.0.0.1:8089/yolo/  or http://127.0.0.1:8089/yoloscreen/ 
   ```
2. Press Enter, the server will return the recognition result in JSON format, for example:
   ```json
   {"answer":"1 monitor, 1 person"}
   ```

### Image Text Recognition
1. Enter the following address in the browser's address bar:
   ```
   http://127.0.0.1:8089/ocr/ 
   ```
2. Press Enter, the server will return the recognition result in JSON format, for example:
   ```json
   {"answer":"Screen recognition result"}
   ```

## Notes
1. Ensure that the computer's camera is connected before running the API server.
2. The API server only supports the `GET` request method.
3. The image recognition results returned by the server are for reference only. If there are inaccuracies, please refer to the actual scene.

## Contribution and Feedback
Contributions and suggestions for improving this project are welcome.

## License
This project is licensed under the MIT open-source license. For details, see the [LICENSE](LICENSE) file.
