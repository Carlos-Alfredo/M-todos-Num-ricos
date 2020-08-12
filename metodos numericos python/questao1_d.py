tabela = [[1,-45,-20,0,0,0,0],[0,20,5,1,0,0,9500],[0,0.04,0.12,0,1,0,40],[0,1,1,0,0,1,551]]
colunas = ["Z","A","B","S1","S2","S3","Solução"]
linhas = ["Z","S1","S2","S3"]
n_colunas=7
n_linhas=4

#Inicio do algoritmo

#Buscar o menor numero negativo na linha 0
menor_posicao=-1
menor_valor=0
for coluna in range(0,n_colunas):
	if(tabela[0][coluna]<menor_valor):
		menor_valor=tabela[0][coluna]
		menor_posicao=coluna
#O menor numero negativo na linha 0 esta na coluna menor_posicao, caso nao haja um numero negativo a posicao é -1
solucao_dividida=[]
while(menor_posicao!=-1): #O loop terminara quando nao houver numero negativo na linha Z
	#Vamos agora dividir a ultima coluna pelos elementos da coluna i em cada linha
	solucao_dividida.clear()
	solucao_dividida.append("Vazio")
	for linha in range (1,n_linhas):
		if(tabela[linha][menor_posicao]==0):
			solucao_dividida.append(float("inf"))
		else:
			solucao_dividida.append(tabela[linha][n_colunas-1]/tabela[linha][menor_posicao])
	#Agora iremos procurar a linha com a menor solucao_dividida positiva
	if(solucao_dividida[1]>0):
		menor_solucao=solucao_dividida[1]
	else:
		menor_solucao=float("inf")
	menor_solucao_posicao=1
	for i in range (1,n_linhas):
		if(solucao_dividida[i]>0 and solucao_dividida[i]<menor_solucao):
			menor_solucao=solucao_dividida[i]
			menor_solucao_posicao=i
	#Agora vamos pegar o elemento tabela[menor_solucao_posicao][menor_posicao] e dividir a linha menor_solucao_posicao por ele
	pivo=tabela[menor_solucao_posicao][menor_posicao]
	for coluna in range(0,n_colunas):
		if(pivo==0):
			tabela[menor_solucao_posicao][coluna]=float("inf")
		else:
			tabela[menor_solucao_posicao][coluna]=tabela[menor_solucao_posicao][coluna]/pivo
	linhas[menor_solucao_posicao]=colunas[menor_posicao] #mudando o cabecalho da tabela
	#Agora vamos pegar a linha menor_solucao_posicao e somar nas demais de forma que a coluna menor_posicao seja zerada em todas as linhas
	#menos na linha menor_solucao_posicao
	for linha in range (0,n_linhas):
		if(linha!=menor_solucao_posicao):
			if(tabela[menor_solucao_posicao][menor_posicao]==0):
				razao=float("inf")
			else:
				razao=tabela[linha][menor_posicao]/tabela[menor_solucao_posicao][menor_posicao]
			for coluna in range (0,n_colunas):
				tabela[linha][coluna]=tabela[linha][coluna]-(razao*tabela[menor_solucao_posicao][coluna])
	#Buscar o menor numero negativo na linha 0
	menor_posicao=-1
	menor_valor=0
	for coluna in range(0,n_colunas):
		if(tabela[0][coluna]<menor_valor):
			menor_valor=tabela[0][coluna]
			menor_posicao=coluna
	#O menor numero negativo na linha 0 esta na coluna menor_posicao, caso nao haja um numero negativo a posicao é -1
	#Caso menor_posicao==-1 o while termina
print(tabela)
for i in range (0,n_linhas):
	print(linhas[i],"=",tabela[i][n_colunas-1])