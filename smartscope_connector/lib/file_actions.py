import shutil
import mrcfile

def save_to_disk(imagebytes, filename:str) -> str:
    with open(filename, 'wb') as f:
        shutil.copyfileobj(imagebytes, f)
    return filename

def read_mrc(filepath):
    with mrcfile.open(filepath,'r') as mrc:
        pixel_size = mrc.header.cella.x/mrc.header.nx
        data = mrc.data
    return pixel_size, data