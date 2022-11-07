import requests

class BackendCommunicator:
    def __init__(self, host, camera_id):
        self.host = host
        self.report_url =self.host + f'/api/v1/cameras/{camera_id}/'

    def send_current_load(self, current_load:int):
        request_body = {
            'current_load':current_load
        }
        response = requests.post(self.report_url, data = request_body)
        print(response)
        return response