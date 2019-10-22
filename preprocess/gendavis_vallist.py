import os
import numpy as np

dataset_folder = '/home/priya/code/data_volume/timecycle'
outlist = os.path.join(dataset_folder, 'davis/DAVIS/vallist.txt')
imgfolder = os.path.join(dataset_folder, 'davis/DAVIS/JPEGImages/480p/')
lblfolder = os.path.join(dataset_folder, 'davis/DAVIS/Annotations/480p/')

jpglist = []

f1 = open(os.path.join(dataset_folder, 'davis/DAVIS/ImageSets/2017/val.txt'), 'r')
for line in f1:
    line = line[:-1]
    jpglist.append(line)
f1.close()


f = open(outlist, 'w')

for i in range(len(jpglist)):

    fname = jpglist[i]
    fnameim = imgfolder + fname + '/'
    fnamelbl= lblfolder + fname + '/'

    if len(os.listdir(fnameim)) > 20:

        f.write(fnameim + ' ' + fnamelbl + '\n')


f.close()
