from FileOperationFactory import FileOperationFactory
from FileOperation import FileOperation
import os

BASE_DIRECTORY = "file_versioning"
BACKUP_DIRECTORY = os.path.join(BASE_DIRECTORY, "backup")
FileOperation.BACKUP_DIRECTORY=BACKUP_DIRECTORY
FileOperation.BASE_DIRECTORY=BASE_DIRECTORY

def initialize_directories():
    os.makedirs(BASE_DIRECTORY, exist_ok=True)
    os.makedirs(BACKUP_DIRECTORY, exist_ok=True)

def main():
    initialize_directories()

    while True:
        print("\n---- File Versioning System Menu ----")
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. List Files")
        print("6. Restore Previous Version")
        print("7. Rollback Changes")
        print("8. Tag Version")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "9":
            print("Exiting...")
            break

        operation = FileOperationFactory.create_operation(choice)
        if operation:
            operation.execute()
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()