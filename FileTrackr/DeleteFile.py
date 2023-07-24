import os
from FileOperation import FileOperation
import time
import shutil

class DeleteFile(FileOperation):
    def execute(self):
        filename = input("Enter the file name: ")
        file_path = os.path.join(self.BASE_DIRECTORY, filename)
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        backup_path = os.path.join(self.BACKUP_DIRECTORY, filename)
        os.makedirs(self.BACKUP_DIRECTORY, exist_ok=True)
        timestamp = int(time.time())
        backup_file_path = os.path.join(self.BACKUP_DIRECTORY, f"{timestamp}_{filename}")
        shutil.copy2(file_path, backup_file_path)

        os.remove(file_path)
        print("File deleted successfully.")