import os


# define the 'data' folder
EXPORT_FOLDER = "data"

# create the folder if it does not exist yet
if not os.path.exists(EXPORT_FOLDER):
    os.mkdir(EXPORT_FOLDER)
    print(f"Folder {EXPORT_FOLDER} does not exist yet.")
    print(f"📂 Created {EXPORT_FOLDER}")