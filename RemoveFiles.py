import os, shutil, time
from sys import path
def main():
    deletedFoldersCount=0
    deletedFilesCount=0
    path="/path_to_delete"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootfolders,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(rootfolders):
                remove_folder(rootfolders)
                deletedFoldersCount+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(rootfolders,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFoldersCount+=1
                for file in files: 
                    file_path=os.path.join(rootfolders,file)
                    if seconds>=get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFilesCount+=1
            else:
                if seconds>=get_file_or_folder_age(path):
                    remove_file(path)
                    deletedFilesCount+=1
    else:
        print(f'"{path}"is not found')
    print(f'total folders deleted:{deletedFoldersCount}')
    print(f'total files deleted:{deletedFilesCount}')

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path}is removed succesfully.")
    else:
        print("Unable to delete the path.")
def remove_file(path):
    if not os.remove(path):
        print(f"{path} removed succesfully.")
    else:
        print("Unable to delete the path.")
def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime 
if __name__="__main__":
    main() 