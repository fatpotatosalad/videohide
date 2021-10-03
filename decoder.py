import os, argparse, cv2
import numpy as np

parser = argparse.ArgumentParser(description='Decodes specially encoded data from video')
parser.add_argument('in_fil', metavar='i', type=str, help='input file')
parser.add_argument('out_dir', metavar='o', type=str, help='output directory')
args = parser.parse_args()

in_path = args.in_fil
out_path = args.out_dir
base_in = os.path.basename(in_path)
out_fil = os.path.join(out_path, os.path.splitext(base_in)[0])

final_barr = b''
video = cv2.VideoCapture(in_path)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

def progress(x):
    prog_steps = 50
    prog_sym = "="
    progress = (x+1)/total_frames
    prog_int = int(progress * 100)
    progress_sp = int(progress * prog_steps)
    print(f'['+ int(progress*prog_steps) * prog_sym + int(prog_steps-progress_sp) * ' ' + f'][{prog_int}%]',end='\r')

with open(out_fil,'wb') as fil:
    cnt = 0
    while video.isOpened():
        success, frame = video.read()
        try:
            fil.write(bytearray(frame.flatten().tolist()))
        except AttributeError:
            break
        progress(cnt)
        cnt += 1
print('\nDone')