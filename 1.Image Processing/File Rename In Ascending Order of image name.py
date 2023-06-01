import os
path2 = "./284"
files = os.listdir(path2)

import re
numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

i =0
for file in sorted(files, key=numericalSort):
        if file.endswith((".jpg")):
            #print (file)
            i+=1
            os.rename(os.path.join(path2, file), os.path.join(path2, ''.join([str(i), '.jpg'])))

