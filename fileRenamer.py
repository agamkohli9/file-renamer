#!/usr/bin/env python
import subprocess
import sys
import pandas as pd

#order for each file
order = ('front', 'back', 'label', 'right', 'left')

#read in data from csv file
sheet = pd.read_csv('sheet.csv')

#get directory of files
dir = input('enter images directory (should look like /Volumes/name_of_device/something): ')

print('Loading...')

#make renamedImages directory
command = ('mkdir', dir + '/../renamedImages')
subprocess.call(command)

#rename files
command = ('ls', dir)
pipe = subprocess.Popen(command, stdout=subprocess.PIPE)

command = ('wc', '-l')
length = int(subprocess.Popen(command, stdin=pipe.stdout, stdout=subprocess.PIPE).stdout.read())

command = ('ls', dir)

for i in range(length):
    #set file names
    i_file = dir + '/' + str(subprocess.Popen(command, stdout=subprocess.PIPE).stdout.read())[2:14]
    o_file = dir + '/../renamedImages/' + sheet.loc[int((i + len(order)) / len(order)) - 1, 'code'] + '.' + order[i % len(order)]

    #do unix command to change file name
    subprocess.call(['mv', i_file, o_file])

#delete empty directory
command = ('rmdir', dir)
subprocess.call(command)

#let user know program is finished
print('Done!')