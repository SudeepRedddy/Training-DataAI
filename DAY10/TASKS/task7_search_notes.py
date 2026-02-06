from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

notes = [
    {"id": 1, "text": "Hello World"},
    {"id": 2, "text": "Python Programming"},
    {"id": 3, "text": "Hello Python"}
]

class SearchHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path == "/notes":
            query_params = parse_qs(parsed_url.query)
            search_query = query_params.get("search", [""])[0].lower()
            
            filtered_notes = [
                note for note in notes 
                if search_query in note["text"].lower()
            ]
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filtered_notes).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SearchHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 7 Server running on http://localhost:{port}/notes?search=word")
    print("Method: GET")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
