# yolo7-stream-count
# Create vitrualenv & install requirements
    virtualenv -p python3 .
    . bin/activate
    pip install -r requirements.txt


# Download weights
    wget https://objects.githubusercontent.com/github-production-release-asset-2e65be/511187726/c0e9f375-a42b-45d5-9e96-3156476cf121?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20221030%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221030T135819Z&X-Amz-Expires=300&X-Amz-Signature=688b65c0e74a45e7db9072f023d2a071cc8c8a912fb9b925ef421c5c8be353d7&X-Amz-SignedHeaders=host&actor_id=10780309&key_id=0&repo_id=511187726&response-content-disposition=attachment%3B%20filename%3Dyolov7x.pt&response-content-type=application%2Foctet-stream

# Run the test 
    ./test.sh