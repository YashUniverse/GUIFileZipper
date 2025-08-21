import zipfile
import pathlib
def make_compress(filepath,dest_dir):
    dest=pathlib.Path(dest_dir,"compress.zip")
    with zipfile.ZipFile(dest,'w') as file:
        file.write(filepath)

if __name__=="__main__":
    make_compress("yash.txt","NewFolder")