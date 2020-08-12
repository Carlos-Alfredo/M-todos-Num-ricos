valor_real=2.6
def funcao(x,y):
	return x*x-2*y*y+x*y*y*y
def trapezio(x,fx):
	return (fx[0]+fx[1])*(x[1]-x[0])/2
def double_trapezio(x0,xf,y0,yf,n):
	x=[]
	for i in range(0,n+1):
		x.append(x0+i*(xf-x0)/n)
	y=[]
	for i in range(0,n+1):
		y.append(y0+i*(yf-y0)/n)
	integral_x=[]
	for i in range(0,n+1):
		integral=0
		for j in range(0,n):
			integral=integral+trapezio([x[j],x[j+1]],[funcao(x[j],y[i]),funcao(x[j+1],y[i])])
		integral_x.append(integral)
	integral=0
	for i in range(0,n):
		integral=integral+trapezio([y[i],y[i+1]],[integral_x[i],integral_x[i+1]])
	return integral
x0=0
xf=2
y0=-1
yf=1
resposta=double_trapezio(x0,xf,y0,yf,4)
print("Utilizando o método do trapézio(n=4) =",resposta,". Erro=",(valor_real-resposta)/valor_real)
##################################################################################################################
def simpson1_3(x,fx):
	return (x[2]-x[0])*(fx[0]+4*fx[1]+fx[2])/6
def double_simpson1_3(x0,xf,y0,yf):
	x=[x0,x0+(xf-x0)/2,xf]
	y=[y0,y0+(yf-y0)/2,yf]
	integral_x=[simpson1_3(x,[funcao(x[0],y[0]),funcao(x[1],y[0]),funcao(x[2],y[0])]),simpson1_3(x,[funcao(x[0],y[1]),funcao(x[1],y[1]),funcao(x[2],y[1])]),simpson1_3(x,[funcao(x[0],y[2]),funcao(x[1],y[2]),funcao(x[2],y[2])])]
	integral=simpson1_3(y,integral_x)
	return integral
resposta=double_simpson1_3(x0,xf,y0,yf)
print("Utilizando uma aplicação única do método 1/3 de Simpson =",resposta,". Erro=",(resposta-valor_real)/valor_real)
##################################################################################################################
def simpson3_8(x,fx):
	return (x[3]-x[0])*(fx[0]+3*fx[1]+3*fx[2]+fx[3])/8
def double_simpson3_8(x0,xf,y0,yf):
	x=[x0,x0+(xf-x0)/3,x0+2*(xf-x0)/3,xf]
	y=[y0,y0+(yf-y0)/3,y0+2*(yf-y0)/3,yf]
	integral_x=[simpson3_8(x,[funcao(x[0],y[0]),funcao(x[1],y[0]),funcao(x[2],y[0]),funcao(x[3],y[0])]),simpson3_8(x,[funcao(x[0],y[1]),funcao(x[1],y[1]),funcao(x[2],y[1]),funcao(x[3],y[1])]),simpson3_8(x,[funcao(x[0],y[2]),funcao(x[1],y[2]),funcao(x[2],y[2]),funcao(x[3],y[2])]),simpson3_8(x,[funcao(x[0],y[3]),funcao(x[1],y[3]),funcao(x[2],y[3]),funcao(x[3],y[3])])]
	integral=simpson3_8(y,integral_x)
	return integral
resposta=double_simpson3_8(x0,xf,y0,yf)
print("Utilizando uma aplicação única do método 3/8 de Simpson =",resposta,". Erro=",(resposta-valor_real)/valor_real)
