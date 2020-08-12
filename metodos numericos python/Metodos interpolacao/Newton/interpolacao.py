import matplotlib.pyplot as plt
def interpolacao(x,fx):#retorna os coeficientes do polinomio interpolado
	tabela=[]
	tabela.append(x)
	tabela.append(fx)
	n_pontos=len(x)
	grau=n_pontos-1
	n_linhas=2
	while(n_pontos>1):
		tabela.append([])
		for coluna in range (0,n_pontos-1):
			x=(tabela[n_linhas-1][coluna+1]-tabela[n_linhas-1][coluna])/(tabela[0][coluna+n_linhas-1]-tabela[0][coluna])
			tabela[n_linhas].append(x)
		n_pontos=n_pontos-1
		n_linhas=n_linhas+1
	b=[]
	for i in range(0,grau+1):
		b.append(tabela[i+1][0])
	return b
def polinomio(x_aprox,x,coeficientes):#calcula f(x_aprox)
	resultado=0
	for i in range(0,len(coeficientes)):
		produto=coeficientes[i]
		for k in range(0,i):
			produto=produto*(x_aprox-x[k])
		resultado=resultado+produto
	return resultado

x=[1.6,2,2.5,3.2,4,4.5]
fx = [2,8,14,15,8,2]

coeficientes=interpolacao(x,fx)
for i in range(0,len(coeficientes)):
	print("b",i,"=",coeficientes[i])

x_aprox=2.8
resultado=polinomio(x_aprox,x,coeficientes)
print("f(",x_aprox,")=",resultado)

#plot do gráfico do polinomio interpolado de f(x)

abcissas=[]
ordenadas=[]
i=0
while(i<5):
	abcissas.append(i)
	ordenadas.append(polinomio(i,x,coeficientes))
	i=i+0.1
plt.plot(abcissas,ordenadas)
plt.show()