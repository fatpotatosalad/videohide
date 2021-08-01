# File to Video Converter

Converts any file into images with bytes as pixel values. And, packs those images into a video.

## Requirements
Used python libraries: 
**argparse**, **numpy**, **PIL**, **shutil**

To intall use:

```bash
pip install shutil numpy pillow argparse
```

Dependencies: **ffmpeg**

If `ffmpeg` is not installed, use:

Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```

Archlinux:
```bash
sudo pacman -S ffmpeg
```

ffmpeg must be added as an environment variable in Windows.
Or, modify the file to include the ffmpeg path.

You might want to follow these steps to install ffmpeg on windows: https://windowsloop.com/install-ffmpeg-windows-10/


## Usage
`encoder.py`
```bash
python encoder.py <input file> <output directory> <output width (optional)> <output height (optional)> <frame rate(optional)>
```

`decoder.py`
```bash
python decoder.py <input file> <output directory>
```

you can also use `-h`
