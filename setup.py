from pathlib import Path
from setuptools import find_packages, setup

HERE = Path(__file__).parent

VERSION = '2.2.1'
PACKAGE_NAME = 'libPyLog' 
AUTHOR = 'Erick Roberto Rodríguez Rodriguez'
AUTHOR_EMAIL = 'erickrr.tbd93@gmail.com, erodriguez@tekium.mx' 
URL = 'https://github.com/erickrr-bd/libPyLog' 

LICENSE = 'GPLv3' 
DESCRIPTION = "Dynamic and secure wrapper built on top of Python's native logging library." 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding ='utf-8')
LONG_DESC_TYPE = "text/markdown"

setup(
    name = PACKAGE_NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = LONG_DESC_TYPE,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = find_packages(),
    include_package_data = True
)