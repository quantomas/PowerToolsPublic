
# start from /home/ubuntu/coco

import os


file_name = '/root/dir/sub/file.ext'

base=os.path.basename(file_name)

base

os.path.splitext(base)

os.path.splitext(base)[0]


## clean

file_name = '/root/dir/sub/image1.jpg'

base=os.path.basename(file_name)

file_name_body = os.path.splitext(base)[0]

file_name_body

ext = 'png'
print(file_name_body + '.' + ext)

###

output_dir = 'infer'
im_name = 'image2.jpg'
ext = 'png'

file_base_name = os.path.basename(im_name)
file_name_body = os.path.splitext(file_base_name)[0]

out_name = os.path.join(output_dir, file_name_body + '.' + ext)

out_name

