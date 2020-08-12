from GaussJordan import GaussJordan
class RegressaoLinearMultipla:
	def __init__(self,x1,x2,y):
		self.n=len(x1)
		s_x1=0
		for i in range(0,self.n):
			s_x1=s_x1+x1[i]
		s_x12=0
		for i in range(0,self.n):
			s_x12=s_x12+x1[i]*x1[i]
		s_x2=0
		for i in range(0,self.n):
			s_x2=s_x2+x2[i]
		s_x22=0
		for i in range(0,self.n):
			s_x22=s_x22+x2[i]*x2[i]
		s_x1x2=0
		for i in range(0,self.n):
			s_x1x2=s_x1x2+x1[i]*x2[i]
		s_y=0
		for i in range(0,self.n):
			s_y=s_y+y[i]
		s_x1y=0
		for i in range(0,self.n):
			s_x1y=s_x1y+y[i]*x1[i]
		s_x2y=0
		for i in range(0,self.n):
			s_x2y=s_x2y+y[i]*x2[i]
		gaussjordan=GaussJordan([[self.n,s_x1,s_x2,s_y],[s_x1,s_x12,s_x1x2,s_x1y],[s_x2,s_x1x2,s_x22,s_x2y]])
		self.solucao=gaussjordan.resolverSistema()
	def funcao(self,x1,x2):
		return self.solucao[0]+self.solucao[1]*x1+self.solucao[2]*x2