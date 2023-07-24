from CreateFile import CreateFile
from ReadFile import ReadFile
from UpdateFile import UpdateFile
from DeleteFile import DeleteFile
from ListFiles import ListFiles
from RestoreVersion import RestoreVersion
from RollbackChanges import RollbackChanges
from TagVersion import TagVersion

class FileOperationFactory:
    @staticmethod
    def create_operation(choice):
        if choice == "1":
            return CreateFile()
        elif choice == "2":
            return ReadFile()
        elif choice == "3":
            return UpdateFile()
        elif choice == "4":
            return DeleteFile()
        elif choice == "5":
            return ListFiles()
        elif choice == "6":
            return RestoreVersion()
        elif choice == "7":
            return RollbackChanges()
        elif choice == "8":
            return TagVersion()
        else:
            return None