import os, argparse, cv2
import numpy as np

parser = argparse.ArgumentParser(description='Encodes files into videos as images')
parser.add_argument('in_fil', metavar='i', type=str, help='input file')
parser.add_argument('out_dir', metavar='o', type=str, help='output directory')
parser.add_argument('im_w', metavar='w', type=int, nargs='?', default=512 , help='image width (optional)')
parser.add_argument('im_h', metavar='h', type=int, nargs='?', default=512, help='image height (optional)')
parser.add_argument('rate', metavar='r', type=float, nargs='?', default=15.0, help='frame_rate (optional)')
args = parser.parse_args()

in_path = args.in_fil
out_path = args.out_dir
base_in = os.path.basename(in_path)
out_fil = os.path.join(out_path, base_in + '.avi')

im_w, im_h = args.im_w, args.im_h
file_size = os.stat(in_path).st_size

bytes_in_row = im_w * 3
bytes_in_frame = int(bytes_in_row * im_h)
total_frames = int(-(-file_size // bytes_in_frame))

fourcc = cv2.VideoWriter_fourcc(*'FFV1')
#'HFYU' is a good alternative but uses too much space
final_video = cv2.VideoWriter(out_fil, fourcc, float(args.rate), (im_w, im_h))

def progress(x):
    prog_steps = 50
    prog_sym = "="
    progress = (x+1)/total_frames
    prog_int = int(progress * 100)
    progress_sp = int(progress * prog_steps)
    print(f'['+ int(progress*prog_steps) * prog_sym + int(prog_steps-progress_sp) * ' ' + f'][{prog_int}%]',end='\r')

with open(in_path,'rb') as input_file:
    for x in range(total_frames):
        raw_barr = bytearray(input_file.read(bytes_in_frame))
        raw_barr += b"\0" * (bytes_in_frame - len(raw_barr))
        np_raw = np.array(raw_barr, dtype=np.uint8)
        video_frame = np_raw.reshape(im_h, im_w, 3)
        final_video.write(video_frame)
        progress(x)

print('\nDone')
