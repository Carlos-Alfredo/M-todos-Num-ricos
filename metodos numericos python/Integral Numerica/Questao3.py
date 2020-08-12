def trapezio(x,fx):
	return (fx[0]+fx[1])*(x[1]-x[0])/2
def simpson1_3(x,fx):
	return (fx[0]+4*fx[1]+fx[2])*(x[2]-x[0])/6
def simpson3_8(x,fx):
	return (fx[0]+3*fx[1]+3*fx[2]+fx[3])*(x[3]-x[0])/8
def integrar(x,fx):
	integral=0
	i=0
	while( i<len(x)-1):
		if(i+3<len(x) and x[i+1]-x[i+0]==x[i+2]-x[i+1] and x[i+2]-x[i+1]==x[i+3]-x[i+2]):
			integral=integral+simpson3_8([x[i],x[i+1],x[i+2],x[i+3]],[fx[i],fx[i+1],fx[i+2],fx[i+3]])
			i=i+2
		elif(i+2<len(x) and x[i+1]-x[i]==x[i+2]-x[i+1]):
			integral=integral+simpson1_3([x[i],x[i+1],x[i+2]],[fx[i],fx[i+1],fx[i+2]])
			i=i+1
		else:
			integral=integral+trapezio([x[i],x[i+1]],[fx[i],fx[i+1]])
		i=i+1
	return integral
x=[1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10]
fx=[5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]
print("Integral=",integrar(x,fx))