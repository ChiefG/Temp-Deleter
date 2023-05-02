import os

username = os.getlogin()
folder = os.path.join("C:/Users", username, "AppData/Local/Temp")

deleted = 0
failed = 0
green = '\033[92m'
red = '\033[91m'
magenta = '\033[95m'
reset = '\033[0m'

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            deleted += 1
        else:
            failed += 1
    except Exception as error:
        failed += 1

print(magenta + """
  _____                     ____ _                            
 |_   _|__ _ __ ___  _ __  / ___| | ___  __ _ _ __   ___ _ __ 
   | |/ _ \ '_ ` _ \| '_ \| |   | |/ _ \/ _` | '_ \ / _ \ '__|
   | |  __/ | | | | | |_) | |___| |  __/ (_| | | | |  __/ |   
   |_|\___|_| |_| |_| .__/ \____|_|\___|\__,_|_| |_|\___|_|   
                    |_|                                       
""" + reset)
print(green + f"Deleted:{reset} {deleted}")
print(red + f"Failed:{reset} {failed}")
print("")
input("Done. Please click Enter to close Program.")
