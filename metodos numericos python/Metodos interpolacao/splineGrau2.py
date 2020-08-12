from GaussJordan import GaussJordan
def splineGrau2(variavel,x,fx):
	n_pontos=len(x)
	n_variaveis=3*(n_pontos-1)-1
	tabela=[]
	#a primeira funcao passa por (x[0],fx[0]) e é uma reta
	equacao=[]
	equacao.append(x[0])
	equacao.append(1)
	for i in range(3,n_variaveis+1):
		equacao.append(0)
	equacao.append(fx[0])
	tabela.append(equacao)
	#a ultima funcao passa por (x[n_pontos-1],fx[n_pontos-1])
	equacao=[]
	for i in range(0,n_variaveis-3):
		equacao.append(0)
	equacao.append(x[n_pontos-1]*x[n_pontos-1])
	equacao.append(x[n_pontos-1])
	equacao.append(1)
	equacao.append(fx[n_pontos-1])
	tabela.append(equacao)
	#as derivadas nos nós anteriores são continuas
	#primeiro nó
	equacao=[]
	equacao.append(1)
	equacao.append(0)
	equacao.append(-2*x[1])
	equacao.append(-1)
	#demais nós
	for j in range(len(equacao),n_variaveis+1):
		equacao.append(0)
	tabela.append(equacao)
	for i in range(2,n_pontos-1):
		equacao=[0,0]
		for j in range(2,i):
			equacao.append(0)
			equacao.append(0)
			equacao.append(0)
		equacao.append(2*x[i])
		equacao.append(1)
		equacao.append(0)
		equacao.append(-2*x[i])
		equacao.append(-1)
		equacao.append(0)
		for j in range(len(equacao),n_variaveis+1):
			equacao.append(0)
		tabela.append(equacao)
	#Os valores da funcao e dos polinomios adjacentes devem ser iguais nos nós interiores
	for i in range(1,n_pontos-1):
		equacao=[]
		if(i==1):
			equacao.append(x[1])
			equacao.append(1)
		else:
			equacao.append(0)
			equacao.append(0)
			for j in range(2,i):
				equacao.append(0)
				equacao.append(0)
				equacao.append(0)
			equacao.append(x[i]*x[i])
			equacao.append(x[i])
			equacao.append(1)
		for j in range(len(equacao),n_variaveis):
			equacao.append(0)
		equacao.append(fx[i])
		tabela.append(equacao)
		equacao2=[]+equacao
		equacao2.pop()
		equacao2.pop()
		equacao2.pop()
		equacao2.pop()
		if(i==1):
			equacao2=[0,0,x[i]*x[i]]+equacao2+[fx[i]]
		else:
			equacao2=[0,0,0]+equacao2+[fx[i]]
		tabela.append(equacao2)
	gaussJordan=GaussJordan(tabela)
	solucao=gaussJordan.resolverSistema()
	solucao=[0]+solucao
	for i in range(1,n_pontos):
		if(variavel<x[i]):
			return (solucao[3*(i-1)]*variavel*variavel+solucao[3*(i-1)+1]*variavel+solucao[3*(i-1)+2])
	return (solucao[3*(n_pontos-2)]*variavel*variavel+solucao[3*(n_pontos-2)+1]*variavel+solucao[3*(n_pontos-2)+2])

