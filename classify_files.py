import os
import shutil

# a dictionary of file prefixes and paths
prefix_to_path = {
    '-m': '/Users/apple/Documents/SFU/Spring 2020/MACM101',
    '-c': '/Users/apple/Documents/SFU/Spring 2020/CRIM101',
    '-h': '/Users/apple/Documents/SFU/Spring 2020/HIST102',
    '-w': '/Users/apple/Documents/Wallpapers',
    '-b': '/Users/apple/Desktop/Books',
    '-p': '/Users/apple/Documents/Videos/private'
}

# change to the folder you want the script to run in
os.chdir('/Users/apple/Downloads/')
moves = 0
for f in os.listdir():
    try:
        first_chars = f[0:2]
        for item in prefix_to_path:
            # move file to corresponding folder if it starts with a preset prefix
            if first_chars == item:
                target_folder = prefix_to_path.get(item)
                # move and rename file, delete prefix from file name
                shutil.move(f, f"{target_folder}/{f.replace(item, '')}")
                print(f'Moved file {f} to {target_folder}')
                moves += 1
    except:
        print('Problem relocating file')
        pass
print(f'{moves} file(s) were moved.')
