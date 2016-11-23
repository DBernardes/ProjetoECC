def algarismoSig(num):
	if 0< num < 1:
		dec = '%1.0e'%(num)
		dec = dec.split('-')
		dec = int(dec[1])
	
	if num > 1:
		dec = 1
    	
	return dec


