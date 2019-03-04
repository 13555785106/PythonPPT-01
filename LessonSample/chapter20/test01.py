import os

path = "/Users/xiaojf/Desktop/11/img"
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, "A%03d.png" % count))
    count += 1
