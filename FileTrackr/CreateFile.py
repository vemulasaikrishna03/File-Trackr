from FileOperation import FileOperation
import os
class CreateFile(FileOperation):
    def execute(self):
        filename = input("Enter the file name: ")
        content = input("Enter the file content: ")

        file_path = os.path.join(self.BASE_DIRECTORY, filename)
        if os.path.exists(file_path):
            print("File already exists.")
            return

        with open(file_path, "w") as file:
            file.write(content)
        print("File created successfully.")