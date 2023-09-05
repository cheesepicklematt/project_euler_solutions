import os

for folder in os.listdir('.'):
    if folder.startswith('q'):
        tmpLen = len(folder[1:])
        if tmpLen==1:
            new_folder_name = 'q00' + folder[1:]
        else:
            new_folder_name = 'q0' + folder[1:]
        os.rename(folder, new_folder_name)