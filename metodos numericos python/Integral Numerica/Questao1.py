import math
import matplotlib.pyplot as plt
def funcao(x):
	return 6 + 3*math.cos(x)
valor_real=6*(math.pi/2)+3*(math.sin(math.pi/2)-math.sin(0))
a=0
b=math.pi/2
def trapezio(n,a,b):
	h=(b-a)/n
	integral=0
	for i in range(0,n):
		integral=integral+(funcao(a+h*i)+funcao(a+h*(i+1)))*h/2
	return integral
def n_trapezio(n,valor_real):
	integrais=[]
	erros=[]
	numero=[]
	for i in range(1,n+1):
		integral=trapezio(i,a,b)
		integrais.append(integral)
		erros.append(math.fabs((integral-valor_real)/valor_real))
		numero.append(i)
	plt.figure(1)
	plt.subplot(211)
	plt.title("Integral através da regra do trapézio")
	plt.plot(numero,integrais)
	plt.xlabel("n")
	plt.ylabel("Integral")
	plt.subplot(212)
	plt.plot(numero,erros)
	plt.xlabel("n")
	plt.ylabel("|%Erro|")
def simpson1_3(n,a,b):
	h=(b-a)/n
	integral=0
	for i in range(0,int(n/2)):
		integral=integral+h/3*(funcao(a+h*(2*i))+4*funcao(a+h*(2*i+1))+funcao(a+h*(2*i+2)))
	return integral
def n_simpson1_3(n,valor_real):
	integrais=[]
	erros=[]
	for i in range(0,len(n)):
		integral=simpson1_3(n[i],a,b)
		integrais.append(integral)
		erros.append(math.fabs((integral-valor_real)/valor_real))
	plt.figure(2)
	plt.subplot(211)
	plt.title("Integral através da regra de 1/3 de Simpson")
	plt.plot(n,integrais)
	plt.yscale('log')
	plt.xlabel("n")
	plt.ylabel("Integral")
	plt.subplot(212)
	plt.plot(n,erros)
	plt.xlabel("n")
	plt.ylabel("|%Erro|")
def simpson3_8(n,a,b):
	h=(b-a)/n
	integral=0
	for i in range(0,int(n/3)):
		integral=integral+3*h/8*(funcao(a+h*(3*i))+3*funcao(a+h*(3*i+1))+3*funcao(a+h*(3*i+2))+funcao(a+h*(3*i+3)))
	return integral
def n_simpson(n,a,b):
	if(n%2==0):
		return simpson1_3(n,a,b)
	elif(n==3):
		return simpson3_8(3,a,b)
	else:
		return simpson1_3(n-3,a,b-3*(b-a)/n)+simpson3_8(3,b-3*(b-a)/n,b)
def simpson(n,valor_real):
	integrais=[]
	erros=[]
	for i in range(0,len(n)):
		integral=n_simpson(n[i],a,b)
		integrais.append(integral)
		erros.append(math.fabs((integral-valor_real)/valor_real))
	plt.figure(3)
	plt.subplot(211)
	plt.title("Integral através das regras de 1/3 e 3/8 de Simpson")
	plt.plot(n,integrais)
	plt.yscale('log')
	plt.xlabel("n")
	plt.ylabel("Integral")
	plt.subplot(212)
	plt.plot(n,erros)
	plt.xlabel("n")
	plt.ylabel("|%Erro|")


n_trapezio(10,valor_real)
n_simpson1_3([2,4,6,8,10],valor_real)
simpson([3, 4, 5, 6, 7, 8, 9, 10],valor_real)
plt.show()