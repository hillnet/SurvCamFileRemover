import os
import time
import sys

path = r"C:\Users\matt-\PycharmProjects\survCamFileRemover\testDirectory"

now = time.time()

for f in os.listdir(path):
    f = os.path.join(path, f)
    if os.stat(f).st_mtime < now:    # - 2 * 86400:
        print(str(f))
        if os.path.isfile(f):
            os.remove(os.path.join(path, f))