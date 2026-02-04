import http.server
import socketserver
import json
import time

PORT = 8080

class BulkRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/list':
            files = [f"dataset_{i}.csv" for i in range(1, 21)] # 20 dummy files
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode('utf-8'))
        
        elif self.path.startswith('/download/'):
            filename = self.path.split('/')[-1]
            chunk = f"Dummy data content for {filename}\n" * 1000 
            data = chunk.encode('utf-8') * 20 
            
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_error(404)

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('127.0.0.1', PORT), BulkRequestHandler) as httpd:
        print(f"Bulk Data Server running on http://127.0.0.1:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
