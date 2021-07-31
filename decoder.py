import os, subprocess, argparse, shutil
import numpy as np
from PIL import Image
from time import sleep

parser = argparse.ArgumentParser(description='Decodes specially encoded data from video')
parser.add_argument('in_fil', metavar='i', type=str, help='input file')
parser.add_argument('out_dir', metavar='o', type=str, help='output directory')
args = parser.parse_args()

in_path = args.in_fil
out_path = args.out_dir
temp_path = os.path.join(out_path, ".temp/")
base_in = os.path.basename(in_path)
out_fil = os.path.join(out_path, os.path.splitext(base_in)[0])

try:
    os.mkdir(temp_path)
except Exception:
    shutil.rmtree(temp_path)
    os.mkdir(temp_path)

subprocess.call(f'ffmpeg -loglevel quiet -i "{in_path}" "{temp_path}%05d.png"')
all_frames = [ temp_path + x for x in os.listdir(temp_path) if '.png' in x ]
all_frames.sort()
final_barr = b''

for cnt, frame in enumerate(all_frames):
    finframe = np.asarray(Image.open(frame))
    final_barr += bytearray(finframe.flatten().tolist())
    print(f"Progress    [{round((cnt/len(all_frames)*100))}%]",end="\r")

with open(out_fil,'wb') as fil:
    fil.write(final_barr)

for x in all_frames:
    os.remove(x)

try:
    os.rmdir(temp_path)
except Exception:
    pass
print("")