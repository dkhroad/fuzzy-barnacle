import json
import re
import os

dict = {}

# skip the .git directory
# Note: it's easier and faster to compute md5sum at the shell level. In Python, I
# probably have to read a large file in chunks.
#
os.system("find . -path \"./.git/*\" -prune -o  -type f -exec md5sum '{}' +  > /tmp/checksums.txt")

with open('/tmp/checksums.txt') as file:
    for line in file:
        values = line.split()
        key = re.sub(r'^\.\/','', values[1])
        # kv.append({re.sub(r'^\.\/','',values[1]): values[0]})
        dict[key] = values[0]

print(json.dumps(dict,indent=4))



