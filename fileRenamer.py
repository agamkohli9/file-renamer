#!/usr/bin/env python
import subprocess
import sys
import pandas as pd

#order for each file
order = ('front', 'back', 'label', 'right', 'left')

#read in data from csv file
sheet = pd.read_csv('sheet.csv')

#input starting and ending image numbers
begin = input('starting number: ')
end = input('ending number: ')

confirmation_str = 'renaming files IMG_' + begin + '.CR2' + ' to ' + 'IMG_' + end + '.CR2 (y/n)'
confirmation = input(confirmation_str)
if confirmation == 'n':
    sys.exit()

#get directory of files
dir = input('enter images directory (should look like /Volumes/name_of_device/something')

print('Loading...')

#rename files
end = int(end)
begin = int(begin)

for i in range(end - begin + 1):
    #set file names
    i_file = dir + 'IMG_' + str(i + begin) + '.CR2'
    o_file = dir + sheet.loc[i, 'code'] + '.' + order[i % 5]

    #do unix command to change file name
    subprocess.call(['mv', i_file, o_file])

#let user know program is finished
print('Done!')