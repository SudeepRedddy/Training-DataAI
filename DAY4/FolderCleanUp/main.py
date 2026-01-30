import os 

folder_path = r"C:\Users\sudee\Downloads\Capgemini\Python\DAY4\FolderCleanUp\cleanup"
for file in os.listdir(folder_path):
    item_path = os.path.join(folder_path,file)
    os.remove(item_path)
    print("Deleted file :",file)
print("File clean Up Succesfull")