import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    # output pathlib ==> dest/compressed.zip
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

#test def function
if __name__ == "__main__":
    make_archive(filepaths = ["question.py", "questions.json"], dest_dir = "dest")




# without def function
#filepaths = ["question.py", "questions.json"]

#output pathlib ==> dest/compressed.zip
#dest_path = pathlib.Path('dest', 'compressed.zip')

#create zip file ==> 'w', extract zip file ==> 'r'
#with zipfile.ZipFile(dest_path, 'w') as archive:
    #for filepath in filepaths :
        #filepath = pathlib.Path(filepath)
        #archive.write(filepath, filepath.name)