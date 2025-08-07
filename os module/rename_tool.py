# Write a program to clear the clutter inside a folder on your computer.
# 2 You should use os module to rename all the png images from 1.png all the
# way till n.png where n is the number of png files in that folder. Do the
# same for other file formats. For example:
# sfdsf.png -- > 1.png
# vfsf.png -- > 2.png
# this.png -- > 3.png
# design.png -- > 4.png
# name.png -- > 5.png

 
import os



print("Current Directory: ", os.getcwd())
os.chdir("os module\images")
print("Current working dir now: ", os.getcwd())


def clean_folder():
    folder_path=os.getcwd()

    try:
        i=1
        files_to_rename=[f for f in os.listdir() if os.path.isfile(f) and f.endswith(".jpg")]
    except FileNotFoundError:
        print(f"Error: The directory {os.getcwd()} was not found or is inaccessible")
        return 
    except FileExistsError:
        if len(files_to_rename)==0:
            print(f"Error : No files in directory")
    finally:
        print(f"Found {len(files_to_rename)} files to proceed in {os.getcwd()}")
        for i in files_to_rename:
            os.rename(i,f"{i}.jpg")
            

    
    # for i in files_to_rename:
        # new_name=os.path.splittext(i)




 
clean_folder()