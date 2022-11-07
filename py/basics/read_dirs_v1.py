
### clean run
# ? tested on Python 3.6.3 64 bit
# cd C:\python\elasticSearch


import json

# dir op's
from os import listdir
from os.path import isfile, isdir, join, splitext, basename


### read from dir
# input_dir = '.\\bilder'
# input_dir = 'bilder'
input_dir = 'C:\\mvs\\output'

files = listdir(input_dir)
files


# onlyfiles = [join(input_dir, f) for f in files ]
onlyfiles = [join(input_dir, f) for f in files if isfile(join(input_dir, f))]
onlyfiles


onlydirs = [join(input_dir, f) for f in files if isdir(join(input_dir, f))]
onlydirs


##

input_dir = 'C:\\mvs\\output'

files = listdir(input_dir)
files

onlydirs = [join(input_dir, f) for f in files if isdir(join(input_dir, f))]
onlydirs

total_images = 0

for firma_dir in onlydirs:
# for firma_dir in onlydirs[0:1]:
    firma_orders = listdir(firma_dir)
    firma_orders = [join(firma_dir, f) for f in firma_orders if isdir(join(firma_dir, f))]
    # print(firma_dir + ' : ' + str(len(firma_orders)))
    print(basename(firma_dir) + ' : ' + str(len(firma_orders)))
    # print(firma_dirs)
    for order_id in firma_orders:
        # print('\t' + order_id)
        print('\t' + basename(order_id))
        
        orders_new = join(order_id, 'new')
        images_new = listdir(orders_new)
        images_new = [join(orders_new, f) for f in images_new if isfile(join(orders_new, f))]
        print('\t\tnew : ' + str(len(images_new)))
        for image in images_new:
            # print('\t\t\t' + image)
            print('\t\t\t' + basename(image))
            total_images +=1
        
        orders_ready = join(order_id, 'ready')
        images_ready = listdir(orders_ready)
        images_ready = [join(orders_ready, f) for f in images_ready if isfile(join(orders_ready, f))]
        print('\t\tready : ' + str(len(images_ready)))
        for image in images_ready:
            # print('\t\t\t' + image)
            print('\t\t\t' + basename(image))
            total_images +=1


# total images
total_images



