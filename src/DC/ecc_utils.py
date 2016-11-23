def readlist(inputlist) :
	with open(inputlist) as f:
   		lines = f.read().splitlines()
	return lines
