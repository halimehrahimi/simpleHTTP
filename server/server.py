
from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class Server(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        with open("db.json", "r") as file:
            data = [json.loads(line) for line in file]
        self.wfile.write(json.dumps(data, indent=4).encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers(status_code=201)
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        try:
            data = json.loads(data_string)
            self.wfile.write(json.dumps(data, indent=4).encode())
            main_x, main_width = data['main']['x'], data['main']['width']
            main_y, main_height = data['main']['y'], data['main']['height']
            for input in data['input']:
                # check if the rectangle intersect with the main rectangle
                if (main_x <= input['x']+input['width'] and main_x+main_width >= input['x']
                    and main_y <= input['y']+input['height'] and main_y+main_height >= input['y']):
                    # datetime object containing current date and time
                    now = datetime.now()
                    # dd/mm/YY H:M:S
                    t_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    # add time to the dictionary
                    input.update(time = t_string)
                    # add the data to a json file
                    with open("db.json", "a") as outfile:
                        json.dump(input, outfile)
                        outfile.write('\n')
                else:
                    pass
            
        except json.JSONDecodeError:
            self._set_headers(status_code=400)
        
        return
