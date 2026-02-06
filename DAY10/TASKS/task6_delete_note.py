from http.server import BaseHTTPRequestHandler, HTTPServer
import json

notes = [{"id": 1, "text": "To be deleted"}]

class DeleteNoteHandler(BaseHTTPRequestHandler):
    def do_DELETE(self):
        if self.path.startswith("/notes/"):
            try:
                note_id = int(self.path.split("/")[-1])
                
                # Find and delete
                for i, note in enumerate(notes):
                    if note["id"] == note_id:
                        del notes[i]
                        self.send_response(204)
                        self.end_headers()
                        return
                
                self.send_response(404)
                self.end_headers()

            except ValueError:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=DeleteNoteHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 6 Server running on http://localhost:{port}/notes/{{id}}")
    print("Method: DELETE")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
