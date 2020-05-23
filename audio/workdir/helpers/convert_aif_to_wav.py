#	Converts AIF input files to WAV

import os
import subprocess

path = os.getcwd() 
print(path)
# In Windows this is the root path is different: We will change it to the right path
os.chdir("C:\\Users\\s157874\\Documents\\GitHub\\open-nsynth-super\\audio\\workdir\\helpers\\sample")
path = os.getcwd()
print(path)

for fname in os.listdir(path):
	nfn = fname.replace('aif', 'wav')
	print(os.listdir(path))
	subprocess.call(["sox", fname, "-b", "16", "-r", "16000", "-c", "1", nfn], shell=True)
	# os.remove(fname)
