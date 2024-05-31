import os

directory_real = "data/real/sp_4"
for filename in os.scandir(directory_real):
    prefix = filename.name.split(".")[0]
    os.rename(filename, prefix + "_sp_4.wav")
