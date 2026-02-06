from http.server import BaseHTTPRequestHandler, HTTPServer
import json

notes = [{"id": 1, "text": "First note"}, {"id": 2, "text": "Second note"}]

class GetNoteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/notes/"):
            try:
                # Extract ID
                note_id_str = self.path.split("/")[-1]
                note_id = int(note_id_str)
                
                # Find note
                note = next((n for n in notes if n["id"] == note_id), None)
                
                if note:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(note).encode())
                else:
                    self.send_response(404)
                    self.end_headers()
            except ValueError:
                # ID is not an integer
                self.send_response(400)
                self.end_headers()

def run(server_class=HTTPServer, handler_class=GetNoteHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 4 Server running on http://localhost:{port}/notes/{{id}}")
    print("Method: GET")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
