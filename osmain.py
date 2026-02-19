import os

base_path = "Downloads"
categories = ["Images","Music","Videos","Docs","Others"]

for category in categories:
    os.makedirs(os.path.join(base_path,category), exist_ok=True)               
  
extension_map = {".jpg":"Images",
                 ".png":"Images",
                 ".jpeg":"Images",
                 ".mp3": "Music",
                 ".mp4": "Videos",
                 ".pdf": "Docs",
                 ".docx": "Docs"}

for file in os.listdir(base_path):                                     #Pick Each Item From Downloads
    if os.path.isfile(os.path.join(base_path,file)):                   #Ignore Folders
        name, ext = os.path.splitext(file)                             #Get Extension of File
        ext = ext.lower()
        if ext in extension_map:                                       #Decide folder name in which folder will be the file 
           folder_name = extension_map[ext]
        else:
           folder_name = "Others"
           
        old_path = os.path.join(base_path, file)                      #Current file location
        new_path = os.path.join(base_path, folder_name, file)         #New file location
        os.rename(old_path, new_path)                                 #Moves the file 
