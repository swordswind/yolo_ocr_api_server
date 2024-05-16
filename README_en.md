# yolo_ocr_api_server
YOLOv8 & EasyOCR Integrated Image Recognition API Server

This project integrates the YOLOv8 image object recognition model developed by ultralytics and the EasyOCR image text recognition model developed by JaidedAI, providing fast and accurate image recognition services.

## Project Source Address
- YOLOv8: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) 
- EasyOCR: [https://github.com/JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR) 

## Installation of Dependencies
   ```
   pip install -r requirements.txt
   ```

## Running Method
python img_api_server.py

## Server Address
The default address for the image recognition model API server is: `http://your computer's IP:8089/`

## API Interface
### Image Object Recognition Model
- **Interface Address**: `/yolo/`
- **Request Method**: `GET`
- **Request Parameters**: None

### Image Text Recognition Model
- **Interface Address**: `/ocr/`
- **Request Method**: `GET`
- **Request Parameters**: None

## Usage Example
### Image Object Recognition
1. Enter the following address in the browser's address bar:
   ```
   http://127.0.0.1:8089/yolo/ 
   ```
2. Press the Enter key, and the server will return the recognition result in JSON format, for example:
   ```json
   {"answer":"1 monitor, 1 person"}
   ```

### Image Text Recognition
1. Enter the following address in the browser's address bar:
   ```
   http://127.0.0.1:8089/ocr/ 
   ```
2. Press the Enter key, and the server will return the recognition result in JSON format, for example:
   ```json
   {"answer":"Screen recognition result"}
   ```

## Notes
1. Ensure that your computer's camera is connected before running the API server.
2. The API server only supports the `GET` request method.
3. The image recognition results returned by the server are for reference only. If there are any inaccuracies, please refer to the actual scene.

## Contributions and Feedback
Suggestions for improvements or contributions to the project are welcome.

## License
This project is licensed under the MIT open-source license. For details, see the [LICENSE](LICENSE) file.
