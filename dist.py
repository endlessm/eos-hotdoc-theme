#!/usr/bin/env python3

import os
import os.path
import shutil
import subprocess
import sys

themedir = sys.argv[1]
srcdir = sys.argv[2]
archivename = sys.argv[3]

for extra in ['images', 'templates']:
    extradir = os.path.join(srcdir, extra)
    for f in os.listdir(extradir):
        shutil.copy(os.path.join(extradir, f), os.path.join(themedir, extra))

distfilename = os.path.join(srcdir, archivename)
cmd = ['tar', '-cJf', distfilename] + os.listdir(themedir)

subprocess.check_call(cmd, cwd=themedir)
