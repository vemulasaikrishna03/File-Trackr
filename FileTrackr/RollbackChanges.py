import os
from FileOperation import FileOperation
import shutil

class RollbackChanges(FileOperation):
    def execute(self):
        filename = input("Enter the file name: ")
        file_path = os.path.join(self.BASE_DIRECTORY, filename)
        if not os.path.exists(file_path):
            print("File does not exist.")
            return

        version_dir = os.path.join(file_path, "versions")
        versions = os.listdir(version_dir)
        if not versions:
            print("No previous versions found.")
            return

        print("Available versions:")
        for i, version in enumerate(versions):
            print(f"{i + 1}. {version}")

        choice = input("Enter the version number to rollback to: ")
        try:
            version_index = int(choice) - 1
            selected_version = versions[version_index]
        except (ValueError, IndexError):
            print("Invalid version number.")
            return

        version_path = os.path.join(version_dir, selected_version)
        shutil.copy2(version_path, file_path)
        print("Changes rolled back successfully.")