from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Dummy data for demonstration
notes = [{"id": 1, "text": "First note"}, {"id": 2, "text": "Second note"}]

class ListNotesHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/notes":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(notes).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=ListNotesHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 3 Server running on http://localhost:{port}/notes")
    print("Method: GET")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
