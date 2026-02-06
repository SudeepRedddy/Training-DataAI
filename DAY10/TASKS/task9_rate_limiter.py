from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
from collections import defaultdict

# Store request timestamps per IP
request_history = defaultdict(list)

class RateLimitHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        current_time = time.time()
        
        # Filter out timestamps older than 60 seconds
        request_history[client_ip] = [
            t for t in request_history[client_ip] 
            if current_time - t < 60
        ]
        
        if len(request_history[client_ip]) >= 5:
            self.send_response(429)
            self.end_headers()
            return
        
        # Add current request timestamp
        request_history[client_ip].append(current_time)
        
        # Handle /health for testing
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RateLimitHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 9 Server running on http://localhost:{port}/health")
    print("Method: GET (Rate Limited)")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
