
import numpy as np
import os

data_path = '/home/priya/code/data_volume/timecycle'
src = os.path.join(data_path, 'manifest_new.txt')
outlist = os.path.join(data_path, 'vlog_frames_12fps.txt')
foldername = '/home/priya/code/data_volume/timecycle/vlog_frames_12fps/'

file = open(src, 'r')
fout = open(outlist, 'w')

for line in file:
    line = line[:-1]
    fname = foldername + line
    print(fname)
    fnms  = len(os.listdir(fname))
    outstr = fname + ' ' + str(fnms) + '\n'
    fout.write(outstr)


file.close()
fout.close()
