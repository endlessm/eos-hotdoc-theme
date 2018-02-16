#!/usr/bin/env python3

import os
import subprocess
import sys

themedir = sys.argv[1]
distfilename = sys.argv[2]

cmd = ['tar', '-cJf', distfilename] + os.listdir(themedir)

subprocess.check_call(cmd, cwd=themedir)
