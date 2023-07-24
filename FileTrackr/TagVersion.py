import os
from FileOperation import FileOperation
import shutil


class TagVersion(FileOperation):
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

        choice = input("Enter the version number to tag: ")
        try:
            version_index = int(choice) - 1
            selected_version = versions[version_index]
        except (ValueError, IndexError):
            print("Invalid version number.")
            return

        tag = input("Enter the tag for this version: ")
        version_path = os.path.join(version_dir, selected_version)
        tagged_version = os.path.join(version_dir, f"{tag}_{selected_version}")
        shutil.copy2(version_path, tagged_version)
        print("Version tagged successfully.")