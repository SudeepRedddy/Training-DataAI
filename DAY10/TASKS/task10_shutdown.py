from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time

class ShutdownHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/shutdown":
            client_ip = self.client_address[0]
            
            # Allow only localhost (IPv4 or IPv6 representation)
            if client_ip not in ["127.0.0.1", "::1"]:
                self.send_response(403)
                self.end_headers()
                return

            self.send_response(200)
            self.end_headers()
            
            print("Shutting down server...")
            threading.Thread(target=self.server.shutdown).start()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=ShutdownHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 10 Server running on http://localhost:{port}/shutdown")
    print("Method: POST")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
