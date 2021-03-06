import argparse
import fnmatch
import glob
import json
import os
import shutil
import subprocess
import uuid

from joblib import delayed
from joblib import Parallel
import pandas as pd

data_path = '/home/priya/code/data_volume/timecycle'
file_src = os.path.join(data_path, 'manifest.txt')
#folder_path = os.path.join(data_path, 'vlog/')
folder_path = os.path.join(data_path, 'vlog/')
print(folder_path)
#output_path = os.path.join(data_path, 'vlog256/')
output_path = os.path.join(data_path, 'vlog256/')
print(output_path)

file_list = []

f = open(file_src, 'r')

for line in f:
    rows = line.split()
    fname = rows[0]
    file_list.append(fname)

f.close()


def download_clip(inname, outname):

    status = False
    #inname = '"%s"' % inname
    #outname = '"%s"' % outname
    print(inname, outname)
    command = "ffmpeg  -loglevel panic -i {} -filter:v scale=\"trunc(oh*a/2)*2:256\" -q:v 1 -c:a copy {}".format( inname, outname)
    try:
        output = subprocess.check_output(command, shell=True,
                                         stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        return status, err.output

    # Check if the video was successfully saved.
    status = os.path.exists(outname)
    print(status)
    return status, 'Downloaded'


def download_clip_wrapper(row):
    """Wrapper for parallel processing purposes."""
    videoname = row

    inname = folder_path  + videoname + 'clip.mp4'
    outname = output_path + videoname

    if os.path.isdir(outname) is False:
        try:
            os.makedirs( outname, 0755 )
        except:
            print(outname)

    outname = outname + 'clip.mp4'


    downloaded, log = download_clip(inname, outname)
    print(downloaded)
    return downloaded

status_lst = Parallel(n_jobs=15)(delayed(download_clip_wrapper)(row) for row in file_list)
