# spython
codigos utiles de python

import os

directorios =os.getcwd().split("\\")
directorio = directorios[len(directorios)-1]
a=os.listdir(".")	
for x in os.listdir("."): os.rename(x, x.replace("Screenshot_", directorio + " "))
