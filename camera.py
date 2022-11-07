from backend_communicator import BackendCommunicator
import threading


class Camera:
    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.values = []
        self.current_load = 0
        self.backend_communicator = BackendCommunicator(host='http://0.0.0.0:8000', camera_id=self.camera_id)

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



