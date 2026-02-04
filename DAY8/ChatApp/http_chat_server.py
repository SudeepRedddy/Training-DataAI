import http.server
import socketserver
import json
import threading

PORT = 8000
messages = []

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ChatRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress default logging to keep console clean

    def do_GET(self):
        if self.path == '/messages':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(messages).encode('utf-8'))
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Chat Server is Running</h1><p>Use the client script to chat.</p>")
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/send':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                messages.append(data)
                
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status": "OK"}')
            except Exception as e:
                self.send_error(400)
        else:
            self.send_error(404)

def start_server():
    server = ThreadedHTTPServer(('127.0.0.1', PORT), ChatRequestHandler)
    print(f"HTTP Chat Server running on http://127.0.0.1:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    start_server()