import matplotlib.pyplot as plt
from splineGrau1 import splineGrau1
from splineGrau2 import splineGrau2
from splineGrau3 import splineGrau3
from splineGrau3 import gerarSpline

def divisores_lagrange(x,fx):
	divisores_lagrange=[]
	for i in range (0,len(x)):
		divisor_lagrange=1
		for j in range(0,len(x)):
			if(j!=i):
				divisor_lagrange=divisor_lagrange*(x[i]-x[j])
		divisores_lagrange.append(divisor_lagrange)
	return divisores_lagrange
def lagrange(variavel,divisores_lagrange,x,fx):
	resposta=0
	for i in range (0,len(x)):
		numerador_lagrange=1
		for j in range (0,len(x)):
			if(j!=i):
				numerador_lagrange=numerador_lagrange*(variavel-x[j])
		resposta=numerador_lagrange*fx[i]/divisores_lagrange[i]+resposta
	return resposta
	
x=[1.6,2,2.5,3.2,4,4.5]
fx=[2,8,14,15,8,2]
divisores_lagrange=divisores_lagrange(x,fx)
resposta=lagrange(2.8,divisores_lagrange,x,fx)
print("Usando Lagrange,f(2.8)=",resposta)
ordenadas=[]
abcissas=[]
for i in range(100,500):
	j=i/100
	ordenadas.append(lagrange(j,divisores_lagrange,x,fx))
	abcissas.append(j)
plt.plot(abcissas,ordenadas, color='black', label='Lagrange')
abcissas.clear()
ordenadas.clear()
resposta=splineGrau1(2.8,x,fx)
print("Usando spline de grau 1,f(2.8)=",resposta)
for i in range(100,500):
	j=i/100
	ordenadas.append(splineGrau1(j,x,fx))
	abcissas.append(j)
plt.plot(abcissas,ordenadas, color='blue', label='Spline de Grau 3')
abcissas.clear()
ordenadas.clear()
resposta=splineGrau2(2.8,x,fx)
print("Usando spline de grau 2,f(2.8)=",resposta)
for i in range(100,500):
	j=i/100
	ordenadas.append(splineGrau2(j,x,fx))
	abcissas.append(j)
plt.plot(abcissas,ordenadas, color='green', label='Spline de Grau 2')
abcissas.clear()
ordenadas.clear()
solucao=splineGrau3(x,fx)
resposta=gerarSpline(solucao,2.8,x)
print("Usando spline de grau 3,f(2.8)=",resposta)
for i in range(100,500):
	j=i/100
	ordenadas.append(gerarSpline(solucao,j,x))
	abcissas.append(j)
plt.plot(abcissas,ordenadas, color='red', label='Spline de Grau 3')
abcissas.clear()
ordenadas.clear()
plt.legend()
plt.show()