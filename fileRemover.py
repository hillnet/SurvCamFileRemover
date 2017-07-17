from win10toast import ToastNotifier
import os
import time
import sys

path = r"C:\Users\matt-\PycharmProjects\survCamFileRemover\testDirectory"

now = time.time()
file_count = 0
for f in os.listdir(path):
    f = os.path.join(path, f)
    if os.stat(f).st_mtime < now:    # - 2 * 86400:
        file_count += 1
        print(str(f))
        if os.path.isfile(f):
            os.remove(os.path.join(path, f))

toaster = ToastNotifier()
toaster.show_toast("Surveillance", str(file_count) + " files deleted", duration=10)