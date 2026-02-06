from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/secret":
            api_key = self.headers.get("X-API-Key")
            
            if api_key == "mykey123":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Access Granted"}).encode())
            else:
                self.send_response(401)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=AuthHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print(f"Task 8 Server running on http://localhost:{port}/secret")
    print("Method: GET")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
