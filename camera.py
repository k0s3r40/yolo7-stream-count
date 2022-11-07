import base64

from backend_communicator import BackendCommunicator
import threading
import numpy as np
import cv2

class Camera:
    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.values = []
        self.current_load = 0
        self.backend_communicator = BackendCommunicator(host='http://0.0.0.0:8000', camera_id=self.camera_id)
        self.overlay = self.get_overlay()
        if self.overlay:
            img = base64.b64decode(self.overlay)
            np_data = np.fromstring(img, np.uint8)
            self.overlay = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

    def _normalize_values(self):
        self.current_load = sum(self.values)//len(self.values)
        print('current_load', self.current_load)
        self.values = []

    def add_to_values(self, value:int):
        self.values.append(value)
        if len(self.values) >= 5:
            self._normalize_values()
            self.send_data_to_backend()


    def send_data_to_backend(self):
        send_data = threading.Thread(target=self.backend_communicator.send_current_load,args=(self.current_load,))
        send_data.start()
        send_data.join()


    def get_overlay(self):
        return self.backend_communicator.get_overlay()


