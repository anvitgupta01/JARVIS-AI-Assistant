# https://tombiebl.hashnode.dev/simple-python-script-to-clean-up-your-desktop

import shutil
import os

desktop = "C:\\Users\\anvit\\Desktop\\"
textFiles = "C:\\Users\\anvit\Desktop\\Git Commits\\Assistant\\Cleaner\\textFiles\\"
pythonFiles = "C:\\Users\\anvit\\Desktop\\Git Commits\\Assistant\\Cleaner\\PythonFiles\\"
imageFiles = "C:\\Users\\anvit\\Desktop\\Git Commits\\Assistant\\Cleaner\\imageFiles\\"

for fname in os.listdir(desktop):
    if (fname.endswith('.jpg')) or (fname.endswith('.png')) or (fname.endswith('.jpeg')):
        shutil.move(desktop+fname,imageFiles+fname)
    elif (fname.endswith('.py')) :
        shutil.move(desktop+fname,pythonFiles+fname)
    elif (fname.endswith('.txt')) :
        shutil.move(desktop+fname,textFiles+fname)

# Other files can also be managed here easily.