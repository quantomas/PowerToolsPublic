
### clean run
# tested on Python 3.6.3 64 bit
# cd C:\python\elasticSearch



# dir op's
from os import listdir
from os.path import isfile, isdir, join, splitext, basename, getctime, getsize

from datetime import datetime
import json


input_dir = 'C:\\mvs\\output'

files = listdir(input_dir)
files

onlydirs = [join(input_dir, f) for f in files if isdir(join(input_dir, f))]
onlydirs


total_images = 0

# for firma_dir in onlydirs:
for firma_dir in onlydirs[0:1]:
    firma_orders = listdir(firma_dir)
    firma_orders = [join(firma_dir, f) for f in firma_orders if isdir(join(firma_dir, f))]
    # print(firma_dir + ' : ' + str(len(firma_orders)))
    print(basename(firma_dir) + ' : ' + str(len(firma_orders)))
    # print(firma_dirs)
    for order_id in firma_orders:
        # print('\t' + order_id)
        print('\t' + basename(order_id))
        
        image_states = ['new', 'ready']
        # image_state = 'new'
        # image_state = 'ready'
        for image_state in image_states:
            orders_state = join(order_id, image_state)
            image_files = listdir(orders_state)
            image_files = [join(orders_state, f) for f in image_files if isfile(join(orders_state, f))]
            print('\t\t' + image_state + ' : ' + str(len(image_files)))
            for image in image_files:
                # print('\t\t\t' + image)
                print('\t\t\t' + basename(image))
                total_images +=1


# total images
total_images


## tests
# https://www.w3resource.com/python-exercises/python-basic-exercise-64.php

import time

time.ctime(ctime_o)


ctime_o = getctime(image)

datetime.fromtimestamp(ctime_o).strftime('%Y-%m-%d %H:%M:%S')
datetime.fromtimestamp(ctime_o).strftime('%Y-%m-%d')
datetime.fromtimestamp(ctime_o).strftime('%Y-%m')

##

getsize(image)


##

image_states = ['new', 'ready']

for image_state in image_states:
    print(image_state)






