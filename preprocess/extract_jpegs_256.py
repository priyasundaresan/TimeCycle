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
folder_path = os.path.join(data_path, 'vlog256')
output_path = os.path.join(data_path, 'vlog_frames_12fps')
#file_src = os.path.join(data_path, 'manifest.txt')
file_src = os.path.join(data_path, 'manifest_new.txt')

file_list = []

f = open(file_src, 'r')
for line in f:
    line = line[:-1]
    file_list.append(line)
f.close()


def download_clip(inname, outname):

    status = False
    #print inname, outname
    command = "ffmpeg  -loglevel panic -i {} -q:v 1 -vf fps=12 {}%06d.jpg".format( inname, outname)
    print(command)
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

    inname = folder_path  + '/' + videoname + 'clip.mp4'
    outname = output_path + '/' +videoname

    if os.path.isdir(outname) is False:
        try:
            os.makedirs( outname, 0755 )
        except:
            print(outname)

    downloaded, log = download_clip(inname, outname)
    return downloaded


# def main(input_csv, output_dir, trim_format='%06d', num_jobs=24, tmp_dir='/tmp/kinetics'):

# if __name__ == '__main__':

status_lst = Parallel(n_jobs=10)(delayed(download_clip_wrapper)(row) for row in file_list)
