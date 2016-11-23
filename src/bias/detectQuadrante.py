import matplotlib.pyplot as plt


def detectQuadrante(x,y):	
	ymin , ymax = plt.ylim()
	xmin , xmax = plt.xlim()
	ymedio = (ymin + ymax)/2
	xmedio = (xmin + xmax)/2
	lenX = len(x)
	i=0
	coordx = None
	coordy = None
	quadrante1=False
	quadrante2=False
	quadrante3=False
	quadrante4=False
	while i < lenX:		
		if ymedio < y[i] < ymax and 0 < x[i] < xmedio:
			quadrante1=True	
		elif ymedio < y[i] < ymax and xmedio < x[i] < xmax:	
			quadrante2=True
		elif 0 < y[i] < ymedio and xmedio < x[i] < xmax:
			quadrante3=True	
		elif 0 < y[i] < ymedio and 0 < x[i] < xmedio:		
			quadrante4=True	
		i+=1	

	if quadrante1:
		coordx = 0.35
		coordy = 0.90
	elif quadrante2:
		coordx = 0.35
		coordy = 0.10		
	elif quadrante3:
		coordx = 0.05
		coordy = 0.10
	elif quadrante4:
		coordx = 0.05
		coordy = 0.90	
	else:
		coordx = 0.05
		coordy = 0.90	
	return coordx, coordy
