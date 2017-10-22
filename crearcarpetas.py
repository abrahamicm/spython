import os
a=os.listdir(".")


for x in range(len(a)) : a[x]=a[x].replace(".mp4", "")

for x in a : os.mkdir(x)
