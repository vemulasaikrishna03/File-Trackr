import os
from FileOperation import FileOperation
import time
import shutil

class UpdateFile(FileOperation):
    def execute(self):
        filename = input("Enter the file name: ")
        file_path = os.path.join(self.BASE_DIRECTORY, filename)
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        new_content = input("Enter the new file content: ")

        version_dir = os.path.join(file_path, "versions")
        os.makedirs(version_dir, exist_ok=True)
        timestamp = int(time.time())
        version_path = os.path.join(version_dir, f"{timestamp}_{filename}")
        shutil.copy2(file_path, version_path)

        with open(file_path, "w") as file:
            file.write(new_content)
        print("File updated successfully.")