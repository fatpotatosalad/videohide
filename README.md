# File to Video Converter

Converts any file into images with bytes as pixel values. And, packs those images into a video.

## Requirements
Used python libraries: 
**numpy**, **cv2**

To intall use:

```bash
pip install opencv-python numpy
```

## Usage
`encoder.py`
```bash
python encoder.py <input file> <output directory> <output width (optional)> <output height (optional)> <frame rate(optional)>
```

`decoder.py`
```bash
python decoder.py <input file> <output directory>
```

you can also use `-h` for help

Note: The output encoded file might be slightly larger.
