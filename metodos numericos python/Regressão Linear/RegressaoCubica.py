from GaussJordan import GaussJordan
class RegressaoCubica:
	def __init__(self,x,y):
		self.n=len(x)
		self.x=x
		self.y=y
		s_x=self.somatorio(x)
		s_y=self.somatorio(y)
		s_xy=0
		for i in range(0,self.n):
			s_xy=s_xy+self.x[i]*self.y[i]
		s_x2=0
		for i in range(0,self.n):
			s_x2=s_x2+self.x[i]*self.x[i]
		s_y2=0
		for i in range(0,self.n):
			s_y2=s_y2+self.y[i]*self.y[i]
		s_x3=0
		for i in range(0,self.n):
			s_x3=s_x3+self.x[i]*self.x[i]*self.x[i]
		s_x4=0
		for i in range(0,self.n):
			s_x4=s_x4+self.x[i]*self.x[i]*self.x[i]*self.x[i]
		s_x5=0
		for i in range(0,self.n):
			s_x5=s_x5+self.x[i]*self.x[i]*self.x[i]*self.x[i]*self.x[i]
		s_x6=0
		for i in range(0,self.n):
			s_x6=s_x6+self.x[i]*self.x[i]*self.x[i]*self.x[i]*self.x[i]*self.x[i]
		s_x2y=0
		for i in range(0,self.n):
			s_x2y=s_x2y+self.x[i]*self.x[i]*self.y[i]
		s_x3y=0
		for i in range(0,self.n):
			s_x3y=s_x3y+self.x[i]*self.x[i]*self.x[i]*self.y[i]
		tabela=[[self.n,s_x,s_x2,s_x3,s_y],[s_x,s_x2,s_x3,s_x4,s_xy],[s_x2,s_x3,s_x4,s_x5,s_x2y],[s_x3,s_x4,s_x5,s_x6,s_x3y]]
		gaussjordan=GaussJordan(tabela)
		self.solucao=gaussjordan.resolverSistema()
	def somatorio(self,vetor):
		resposta=0
		for i in range(0,len(vetor)):
			resposta=resposta+vetor[i]
		return resposta
	def funcao(self,x):
		resposta=self.solucao[0]+self.solucao[1]*x+self.solucao[2]*x*x+self.solucao[3]*x*x*x
		return resposta