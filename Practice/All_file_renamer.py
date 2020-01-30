import os
from pathlib import Path
import glob
from shutil import copyfile, copy2

def main():
    try:
        parentdir = Path(__file__).parent #get directory
        path = os.path.join(parentdir, 'data')
        list_of_files = glob.glob(path+'/*.txt')           # create the list of all files inside folder
        for i, file_name in enumerate(list_of_files, start=1):
            os.rename(file_name, path+'//'+str(i)+'.txt') 
            print(file_name)
    except FileExistsError:
        print('File already exist')
        
if __name__ == '__main__':
    main()