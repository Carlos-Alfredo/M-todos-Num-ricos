import math
import matplotlib.pyplot as plt
def funcao(x):
	return x*x*math.exp(x)
valor_real=5*math.exp(3)-2
a=0
b=3
def trapezio(n,a,b):
	h=(b-a)/n
	integral=0
	for i in range(0,n):
		integral=integral+(funcao(a+h*i)+funcao(a+h*(i+1)))*h/2
	return integral
def n_trapezio(valor_real):
	integrais=[]
	erros=[]
	numero=[]
	n=0
	erro=1
	while(erro>0.01):
		n=n+1
		integral=trapezio(n,a,b)
		integrais.append(integral)
		erro=math.fabs((integral-valor_real)/valor_real)
		erros.append(erro)
		numero.append(n)
	print("Número de intervalos necessários para que o método do trapézio tenha um erro menor que 0.01=",n)
	print("Erro=",erro)
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
def n_simpson1_3(valor_real):
	integrais=[]
	n=0
	erro=1
	erros=[]
	numero=[]
	while(erro>0.01):
		n=n+2
		integral=simpson1_3(n,a,b)
		integrais.append(integral)
		erro=(integral-valor_real)/valor_real
		erros.append(math.fabs(erro))
		numero.append(n)
	print("Número de intervalos necessários para que o método do 1/3 de Simpson tenha um erro menor que 0.01=",n)
	print("Erro=",erro)
	plt.figure(2)
	plt.subplot(211)
	plt.title("Integral através da regra de 1/3 de Simpson")
	plt.plot(numero,integrais)
	plt.xlabel("n")
	plt.ylabel("Integral")
	plt.subplot(212)
	plt.plot(numero,erros)
	plt.xlabel("n")
	plt.ylabel("|%Erro|")
n_trapezio(valor_real)
n_simpson1_3(valor_real)
plt.show()
