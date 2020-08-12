def funcao(x,y,z):
	return x*x*x-3*y*z
def simpson1_3(x,fx):
	return (x[2]-x[0])*(fx[0]+4*fx[1]+fx[2])/6
def triple_simpson1_3(x0,xf,y0,yf,z0,zf):
	x=[x0,(x0+xf)/2,xf]
	y=[y0,(y0+yf)/2,yf]
	z=[z0,(z0+zf)/2,zf]
	integral=0
	integral_y=[]
	for i in range(0,3):
		integral_x=[]
		for k in range(0,3):
			integral_x.append(simpson1_3(x,[funcao(x[0],y[k],z[i]),funcao(x[1],y[k],z[i]),funcao(x[2],y[k],z[i])]))
		integral_y.append(simpson1_3(y,integral_x))
	return simpson1_3(z,integral_y)
x0=-3
xf=1
y0=0
yf=2
z0=-2
zf=2
print("Integral tripla usando a regra 1/3 de Simpson = ",triple_simpson1_3(x0,xf,y0,yf,z0,zf))
