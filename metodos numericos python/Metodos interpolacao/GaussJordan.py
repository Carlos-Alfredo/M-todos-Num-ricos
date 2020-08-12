class GaussJordan:
	def __init__(self,tabela):
		self.tabela=tabela
	def resolverSistema(self):
		n_linhas=len(self.tabela)
		n_colunas=len(self.tabela[0])
		linha=0
		while(linha<n_linhas):
			if(self.tabela[linha][linha]!=0):
				q=self.tabela[linha][linha]
				for coluna in range (0,n_colunas):
					self.tabela[linha][coluna]=self.tabela[linha][coluna]/q
				for linha_ in range (0,n_linhas):
					if(linha_!=linha):
						q=self.tabela[linha_][linha]
						for coluna_ in range (0,n_colunas):
							self.tabela[linha_][coluna_]=self.tabela[linha_][coluna_]-q*self.tabela[linha][coluna_]
				linha=linha+1
			else:
				for linha_ in range (linha,n_linhas):
					if(self.tabela[linha_][linha]!=0):
						for coluna_ in range(0,n_colunas):
							self.tabela[linha][coluna_]=self.tabela[linha][coluna_]+self.tabela[linha_][coluna_]
							self.tabela[linha_][coluna_]=self.tabela[linha][coluna_]-self.tabela[linha_][coluna_]
							self.tabela[linha][coluna_]=self.tabela[linha][coluna_]-self.tabela[linha_][coluna_]
						linha_=n_linhas
		solucao=[]
		for i in range(0,n_linhas):
			solucao.append(self.tabela[i][n_colunas-1])
		return solucao