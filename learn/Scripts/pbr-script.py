#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pbr==1.8.1','console_scripts','pbr'
__requires__ = 'pbr==1.8.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pbr==1.8.1', 'console_scripts', 'pbr')()
    )
