import os

username = os.getlogin()
folder = os.path.join("C:/Users",username, "AppData/Local/Temp")

deleted = 0

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            deleted += 1
    except Exception as error:
        print(f"Error deleting file: {error}")

print(f"{deleted} files were deleted from the temporary folder.")

input("Done. Please click Enter to close Program.")