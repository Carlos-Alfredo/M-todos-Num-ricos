x=[1.6,2,2.5,3.2,4,4.5]
fx=[2,8,14,15,8,2]
def splineGrau1(variavel,x,fx):
	resposta=10000
	if(variavel<=x[0]):
		resposta=fx[0]+((fx[1]-fx[0])/(x[1]-x[0]))*(variavel-x[0])
	elif(variavel>=x[len(x)-1]):
		resposta=fx[len(x)-2]+((fx[len(x)-1]-fx[len(x)-2])/(x[len(x)-1]-x[len(x)-2]))*(variavel-x[len(x)-2])
	else:
		for i in range(0,len(x)-1):
			if(variavel>=x[i] and variavel<=x[i+1]):
				resposta=fx[i]+((fx[i+1]-fx[i])/(x[i+1]-x[i]))*(variavel-x[i])
	return resposta

