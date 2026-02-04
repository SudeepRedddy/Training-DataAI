import os
import urllib.request
import json
import time
from concurrent.futures import ThreadPoolExecutor

SERVER_URL = "http://127.0.0.1:8080"
DOWNLOAD_DIR = "bulk_downloads"

def download_file(filename):
    url = f"{SERVER_URL}/download/{filename}"
    save_path = os.path.join(DOWNLOAD_DIR, filename)
    
    print(f"[START] Downloading {filename}...")
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            with open(save_path, 'wb') as f:
                f.write(content)
        print(f"[DONE] Saved {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"[ERROR] Failed {filename}: {e}")

def start_bulk_download():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
        
    print(f"Connecting to {SERVER_URL} to fetch file list...")
    try:
        with urllib.request.urlopen(f"{SERVER_URL}/list") as response:
            files = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Server connection failed: {e}")
        return

    print(f"Found {len(files)} files. Starting parallel download...")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, files)
        
    duration = time.time() - start_time
    print(f"\nAll downloads completed in {duration:.2f} seconds.")
    print(f"Files saved in '{os.path.abspath(DOWNLOAD_DIR)}'")

if __name__ == "__main__":
    start_bulk_download()
