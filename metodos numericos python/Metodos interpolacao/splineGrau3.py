from GaussJordan import GaussJordan
def splineGrau3(x,fx):
	n_pontos=len(x)
	n_variaveis=4*(n_pontos-1)
	tabela=[]
	n_colunas=n_variaveis+1
	#polinomio anterior e posterior aos pontos internos sao continuos
	for i in range(1,n_pontos-1):
		#ponto anterior
		equacao=[]
		for j in range(1,i):
			equacao=[0,0,0,0]+equacao
		equacao=equacao+[x[i]*x[i]*x[i],x[i]*x[i],x[i],1]
		while(len(equacao)<n_colunas-1):
			equacao=equacao+[0]
		equacao=equacao+[fx[i]]
		tabela.append(equacao)
		#ponto posterior
		equacao=[]
		for j in range(0,i):
			equacao=[0,0,0,0]+equacao
		equacao=equacao+[x[i]*x[i]*x[i],x[i]*x[i],x[i],1]
		while(len(equacao)<n_colunas-1):
			equacao=equacao+[0]
		equacao=equacao+[fx[i]]
		tabela.append(equacao)
	#a primeira funcao deve passar por x[0],fx[0]
	equacao=[x[0]*x[0]*x[0],x[0]*x[0],x[0],1]
	while(len(equacao)<n_colunas-1):
		equacao=equacao+[0]
	equacao=equacao+[fx[0]]
	tabela.append(equacao)
	#a ultima funcao deve passar por x[n_pontos-1],fx[n_pontos-1]
	equacao=[x[n_pontos-1]*x[n_pontos-1]*x[n_pontos-1],x[n_pontos-1]*x[n_pontos-1],x[n_pontos-1],1,fx[n_pontos-1]]
	while(len(equacao)<n_colunas):
		equacao=[0]+equacao
	tabela.append(equacao)
	#as primeiras derivadas nos nós interiores devem ser iguais
	for i in range(1,n_pontos-1):
		equacao=[]
		for j in range (1,i):
			equacao=[0,0,0,0]+equacao
		equacao=equacao+[3*x[i]*x[i],2*x[i],1,0,-3*x[i]*x[i],-2*x[i],-1,0]
		while(len(equacao)<n_colunas):
			equacao=equacao+[0]
		tabela.append(equacao)
	#as segundas derivadas nos nós anteriores devem ser iguais
	for i in range(1,n_pontos-1):
		equacao=[]
		for j in range (1,i):
			equacao=[0,0,0,0]+equacao
		equacao=equacao+[6*x[i],2,0,0,-6*x[i],-2,0,0]
		while(len(equacao)<n_colunas):
			equacao=equacao+[0]
		tabela.append(equacao)
	#segunda derivada em x[0],fx[0] é zero
	equacao=[6*x[0],2,0,0]
	while(len(equacao)<n_colunas):
		equacao=equacao+[0]
	tabela.append(equacao)
	#segunda derivada em x[n_pontos-1],fx[n_pontos-1] é zero
	equacao=[6*x[n_pontos-1],2,0,0]
	while(len(equacao)<n_colunas):
		equacao=[0]+equacao
	tabela.append(equacao)
	gaussJordan=GaussJordan(tabela)
	solucao=gaussJordan.resolverSistema()
	return solucao
def gerarSpline(solucao,variavel,x):
	n_pontos=len(x)
	for i in range(1,n_pontos):
		if(variavel<x[i]):
			return (solucao[4*(i-1)]*variavel*variavel*variavel+solucao[4*(i-1)+1]*variavel*variavel+solucao[4*(i-1)+2]*variavel+solucao[4*(i-1)+3])
	return (solucao[4*(n_pontos-2)]*variavel*variavel*variavel+solucao[4*(n_pontos-2)+1]*variavel*variavel+solucao[4*(n_pontos-2)+2]*variavel+solucao[4*(n_pontos-2)+3])
