# yolo7-stream-count
# Create vitrualenv & install requirements
    virtualenv -p python3 .
    . bin/activate
    pip install -r requirements.txt


# Download weights
    wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt

# Run the test 
    ./test.sh
   
# Run the Project
   python detect.py --weights yolov7x.pt --no-trace --conf 0.15  --source http://77.103.172.17:8080/mjpg/video.mjpg --camera-id 1
   
# Video feed
   http://77.103.172.17:8080/mjpg/video.mjpg
