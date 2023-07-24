from FileOperation import FileOperation
import os


class ListFiles(FileOperation):
    def execute(self):
        files = os.listdir(self.BASE_DIRECTORY)
        if files:
            print("Available files:")
            for file in files:
                print(file)
        else:
            print("No files found.")