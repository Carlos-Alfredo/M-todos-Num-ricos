def trapezio(x,fx):
	return (fx[0]+fx[1])*(x[1]-x[0])/2
def simpson1_3(x,fx):
	return (fx[0]+4*fx[1]+fx[2])*(x[2]-x[0])/6
def integrar_trapezio(x,fx):
	integral=0
	for i in range(0,len(x)-1):
		integral=integral+trapezio([x[i],x[i+1]],[fx[i],fx[i+1]])
	return integral
def integrar_simpson1_3(x,fx):
	integral=0
	for i in range(0,int((len(x)-1)/2)):
		integral=integral+simpson1_3([x[2*i],x[2*i+1],x[2*i+2]],[fx[2*i],fx[2*i+1],fx[2*i+2]])
	return integral
x=[1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10]
fx=[5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]
print("Integral pelo método do trapézio=",integrar_trapezio(x,fx))
print("Integral pelo método de 1/3 de Simpson=",integrar_simpson1_3(x,fx))