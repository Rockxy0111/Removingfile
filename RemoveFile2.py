import shutil

path=input(r"Enter the path")

if shutil.path.exists(path):


    shutil.rmtree(path)
    print("Folder, SubFolder and Files within the folder successfully deleted")

else:
    print("The Path dont exists")