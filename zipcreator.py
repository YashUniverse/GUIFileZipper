import zipfile
import pathlib
def make_compress(filepath,dest_dir):
    dest=pathlib.Path(dest_dir,"compress.zip")
    print(type(dest))
    with zipfile.ZipFile(dest,'w') as file:
        for fil in filepath:
            file.write(fil,arcname=pathlib.Path(fil).name)

if __name__=="__main__":
    fun=["functions.py","fitsteal.py"]
    make_compress(fun,"NewFolder")