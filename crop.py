import glob
import skimage.io as io
files = glob.glob("frames/*.png")
files.sort()
for f in files:
    img = io.imread(f)
    io.imsave(f, img[400:, :-10])
