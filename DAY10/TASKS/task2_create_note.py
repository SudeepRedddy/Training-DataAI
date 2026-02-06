from http.server import BaseHTTPRequestHandler, HTTPServer
import json

notes = []

class NoteHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/notes":
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self.send_response(400)
                self.end_headers()
                return

            try:
                body = json.loads(self.rfile.read(content_length))
                if "text" not in body:
                    self.send_response(400)
                    self.end_headers()
                    return
                
                note = {"id": len(notes) + 1, "text": body["text"]}
                notes.append(note)
                
                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(note).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()

def run(server_class=HTTPServer, handler_class=NoteHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 2 Server running on http://localhost:{port}/notes")
    print("Method: POST")
    httpd.serve_forever()

if __name__ == "__main__":
    run()