import os
import cv2
import numpy as np
from tqdm import tqdm
import shutil
import pathlib
import argparse

src_root = "G:\\My Drive\\Senior Project\\dataset\\IP7_small"
dst_root = "G:\\My Drive\\Senior Project\\dataset\\IP7_small_out"

stride = 1


def get_path_list(src_root):
    file_paths = []
    for root, _, fnames in os.walk(src_root):
        for fname in fnames:
            file_paths.append(f'{root}\\{fname}')
    return file_paths

def preprocess_directory(file_paths, dst_root, stride=1): 
    with tqdm(total = len(file_paths)) as pbar:
        for folder_index, file_path in enumerate(file_paths):
            cap = cv2.VideoCapture(file_path)
            i = 0
            processed_i = 0
            N = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            print('File path:', file_path)
            print('Frames:'.format(N))
            
            subdir_path = pathlib.Path(f'{dst_root}\\{folder_index}')
            if subdir_path.exists() and subdir_path.is_dir():
                shutil.rmtree(subdir_path)
            os.mkdir(subdir_path)
            
            
            while cap.isOpened():
                ret, frame = cap.read()
                if ret == False:
                    break

                if i%stride == 0:
                    cv2.imwrite(f'{dst_root}\\{folder_index}\\{folder_index}_{i}.jpg', frame)
                    processed_i += 1
                
                i += 1
            cap.release()
            print('Finish preproess', file_path)
            pbar.update(1)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Extract video script.')
    parser.add_argument('src',
                        help='source root directory')
    parser.add_argument('dst',
                        help='destination root directory')
    parser.add_argument('--stride','-S', default=1)
                    
    args = parser.parse_args()

    src_root = args.src
    dst_root = args.dst
    stride = args.stride

    
    # print(src_root, dst_root, stride)

    file_paths = get_path_list(src_root)

    print('source root directory:',src_root)
    print('destination root directory:',dst_root)
    print('stride:', stride)
    print(f'Total {len(file_paths)} videos')

    preprocess_directory(file_paths=file_paths, dst_root=dst_root, stride=stride)