import os
import shutil
import math
import zipfile

# Function to split the victims.txt file
def split_victims(file_path, num_instances):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    chunk_size = math.ceil(len(lines) / num_instances)
    for i in range(num_instances):
        chunk = lines[i * chunk_size: (i + 1) * chunk_size]
        with open(f'{folder_prefix}{i + 1}/victims.txt', 'w') as outfile:
            outfile.writelines(chunk)

def create_folders_and_copy_files(num_instances):
    created_folders = []
    for i in range(1, num_instances + 1):
        folder_name = f'{folder_prefix}{i}'
        os.makedirs(folder_name, exist_ok=True)
        created_folders.append(folder_name)
        
        # Copy all directories and files except mgbaja.py and folders named 'send'
        for item in os.listdir():
            if item == 'mgbaja.py' or item == os.path.basename(__file__) or item.startswith(folder_prefix):
                continue
            src_path = os.path.join(os.getcwd(), item)
            dest_path = os.path.join(folder_name, item)
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy(src_path, dest_path)
    
    return created_folders

def zip_folder(folder_name):
    shutil.make_archive(folder_name, 'zip', folder_name)

def delete_folders(folders):
    for folder in folders:
        shutil.rmtree(folder)

def main():
    global folder_prefix
    folder_prefix = input("Enter the name to use for appending the folder names: ")
    num_instances = int(input("Enter the number of instances to run: "))
    
    # Create folders and copy files
    created_folders = create_folders_and_copy_files(num_instances)
    
    # Split victims.txt file
    split_victims('victims.txt', num_instances)
    
    # Zip and delete each folder
    for folder_name in created_folders:
        zip_folder(folder_name)
        delete_folders([folder_name])

if __name__ == "__main__":
    main()