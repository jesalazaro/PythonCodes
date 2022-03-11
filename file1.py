import os
entries = os.scandir("files/")

for entry in entries:
    print(entry.name + ", es directorio: " + str(entry.is_dir()) + ", size: " + str(entry.stat().st_size) + "bytes.")
