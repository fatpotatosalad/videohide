import os, sys, subprocess, argparse, shutil
import numpy as np
from PIL import Image

parser = argparse.ArgumentParser(description='Encodes files into videos as images')
parser.add_argument('in_fil', metavar='i', type=str, help='input file')
parser.add_argument('out_dir', metavar='o', type=str, help='output directory')
parser.add_argument('im_w', metavar='w', type=int, nargs='?', default=512 , help='image width (optional)')
parser.add_argument('im_h', metavar='h', type=int, nargs='?', default=512, help='image height (optional)')
parser.add_argument('rate', metavar='r', type=int, nargs='?', default=15, help='frame_rate (optional)')
args = parser.parse_args()

in_path = args.in_fil
out_path = args.out_dir
temp_path = os.path.join(out_path, ".temp")
base_in = os.path.basename(in_path)
out_fil = os.path.join(out_path,base_in)

im_w, im_h = args.im_w, args.im_h

try:
    os.mkdir(temp_path)
except FileExistsError:
    shutil.rmtree(temp_path)
    os.mkdir(temp_path)
os.chdir(temp_path)

input_file = open(in_path, 'rb')
file_size = os.stat(in_path).st_size

bytes_in_row = im_w * 3
bytes_in_frame = int(bytes_in_row * im_h)
total_frames = int(-(-file_size // bytes_in_frame))
byarr_list = list()

for x in range(total_frames):
    raw_barr = bytearray(input_file.read(bytes_in_frame))
    raw_barr += b"\0" * (bytes_in_frame-len(raw_barr))
    byarr_list.append(raw_barr)

input_file.close()

for count, frame in enumerate(byarr_list):
    np_byarr_list = np.array(frame,dtype=np.uint8)
    np_byarr_list =  np_byarr_list.reshape(im_w,im_h,3)
    Image.fromarray(np_byarr_list).save(f"{count+1:05d}.png")
    print(f"Progress    [{round((count/total_frames)*100)}%]",end="\r")

command = f'ffmpeg -loglevel quiet -framerate {args.rate} -i "{temp_path}\\%05d.png" -c:v libx264rgb -qp 0 "{out_fil}.avi"'
subprocess.call(command)

shutil.rmtree(temp_path, ignore_errors=True)

print("")