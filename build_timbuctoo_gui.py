import subprocess
import urllib.request
import urllib.parse
from vistir import create_tracked_tempdir, cd
import os
import tarfile
import sys

TIMBUCTOO_GUI_URL = 'https://github.com/HuygensING/timbuctoo-gui/archive/v5.7.tar.gz'
EXPECTED_FILE_NAME = 'timbuctoo-gui-5.7'

url = urllib.parse.urlparse(TIMBUCTOO_GUI_URL)
basename = os.path.basename(url.path)
#temp_dir = create_tracked_tempdir(prefix='build_timbuctoo_gui')
temp_dir = "/tmp/foo"

# This hackery is needed because some files may have 0600 permissions or
# whatever and tarfile will break in this case
def extract_tar(path):
    tar = tarfile.open(path, 'r:gz', errorlevel=1)
    for file_ in tar:
        try:
            tar.extract(file_)
        except IOError as e:
            os.remove(file_.name)
            tar.extract(file_)
        finally:
            os.chmod(file_.name, file_.mode)
    tar.close()


with cd(temp_dir):
    urllib.request.urlretrieve(TIMBUCTOO_GUI_URL, basename)
    extract_tar(basename)
    
    with cd(EXPECTED_FILE_NAME):
        subprocess.check_call(["npm", "install"], stdout=subprocess.DEVNULL)
        subprocess.check_call(["npm", "run", "build"], stdout=subprocess.DEVNULL)

        with cd("build"):
            with tarfile.open(fileobj=sys.stdout.buffer, mode='w|') as tar:
                for path in os.listdir():
                    tar.add(path, recursive=True)
                
