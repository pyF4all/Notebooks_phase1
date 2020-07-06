"""
@author: Horacio V. Guzman
@project: pyF4all
@date: 11.05.2020

horacio.v.g@gmail.com
"""
import sys
import re
import numpy
import glob

#DATA loading from the small system runs in a cluster

def subit(msg,string):
	subbed = re.sub(string, " ", msg)
	return subbed

def getIndex(string1,cocorico):
	strT1=[]
	for msg in cocorico:
	    strT1.append(subit(msg,string1))
	string2="(.out?)"
	strT2=[]
	for msg in strT1:
	    strT2.append(subit(msg,string2))

	# Final index assignation
	a1=[]
	print(len(strT2))
	for msg in strT2:
	    a=[int(s) for s in re.findall(r'\b\d+\b', msg)]
	    a1.append(a[0])
	procInd0=numpy.asarray(a1)
	return procInd0

# strings to search

def getEnergyInd(set0,string2sH):
	auxT=r'\b'+string2sH
	sarsCoV2solv=[]
	sarsCoV2solvInd=[]
	for filenamePF in glob.glob(set0):
		try:
			with open (filenamePF, 'rt') as in_file:
				for line in in_file:
					aux=re.findall(str(auxT),line)
					if aux!=[]:
						pattern = re.compile(r"[^-\d]*([\-]{0,4}\d+\.\d+)[^-\d]*")
						results = []
						line2=line[18:]
						match = pattern.match(line2)
						if match:
							results.append(match.groups()[0])
						sarsCoV2solv.append(float(results[0]))
						sarsCoV2solvInd.append(filenamePF)
		except:
			pass
	return sarsCoV2solvInd,sarsCoV2solv
