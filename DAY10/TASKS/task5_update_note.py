from http.server import BaseHTTPRequestHandler, HTTPServer
import json

notes = [{"id": 1, "text": "Original note"}]

class UpdateNoteHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        if self.path.startswith("/notes/"):
            try:
                note_id = int(self.path.split("/")[-1])
                
                content_length = int(self.headers.get('Content-Length', 0))
                if content_length == 0:
                    self.send_response(400)
                    self.end_headers()
                    return

                body = json.loads(self.rfile.read(content_length))
                if "text" not in body:
                    self.send_response(400)
                    self.end_headers()
                    return

                # Find and update
                for note in notes:
                    if note["id"] == note_id:
                        note["text"] = body["text"]
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps(note).encode())
                        return
                
                self.send_response(404)
                self.end_headers()

            except ValueError:
                self.send_response(400)
                self.end_headers()
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()

def run(server_class=HTTPServer, handler_class=UpdateNoteHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 5 Server running on http://localhost:{port}/notes/{{id}}")
    print("Method: PUT")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
