import shutil
import os
from datetime import date

src = "C:/Users/sudee/Downloads/Capgemini/Python/DAY4/Automatic file backup/MAIN"
dst = "C:/Users/sudee/Downloads/Capgemini/Python/DAY4/Automatic file backup/BACKUP"

today = date.today().strftime("%d-%m-%Y")
backup_path = os.path.join(dst, f"BackUp_{today}")

if not os.path.exists(backup_path):
    shutil.copytree(src, backup_path)
    print("Backup Successful!")
else:
    print("Backup already exists for today!")
