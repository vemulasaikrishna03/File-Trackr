import os
from FileOperation import FileOperation
class ReadFile(FileOperation):
    def execute(self):
        filename = input("Enter the file name: ")
        file_path = os.path.join(self.BASE_DIRECTORY, filename)
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        with open(file_path, "r") as file:
            content = file.read()
            print(f"File content:\n{content}")