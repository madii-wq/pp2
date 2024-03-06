import os

directory_path = "copied.txt"

if os.path.isfile(directory_path):
    
    with open(directory_path, 'r', encoding='utf-8') as file:
        
        content = file.readlines()
        
        for line in content:
            print(line.strip()) 
else:
    print("File", directory_path, "does not exist.")
