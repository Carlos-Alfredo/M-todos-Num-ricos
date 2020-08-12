import matplotlib.pyplot as plt
import math
class RegressaoLinear:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.n=len(self.x)
		s_x=self.somatorio(x)
		s_y=self.somatorio(y)
		s_xy=0
		for i in range(0,self.n):
			s_xy=s_xy+self.y[i]*self.x[i]
		s_x2=0
		for i in range(0,self.n):
			s_x2=s_x2+self.x[i]*self.x[i]
		s_y2=0
		for i in range(0,self.n):
			s_y2=s_y2+self.y[i]*self.y[i]
		self.coeficiente_angular=(self.n*s_xy-s_x*s_y)/(self.n*s_x2-s_x*s_x)
		self.coeficiente_linear=s_y/self.n-self.coeficiente_angular*s_x/self.n
		self.r=(self.n*s_xy-s_x*s_y)/(math.sqrt((self.n*s_x2-s_x*s_x)*(self.n*s_y2-s_y*s_y)))
	def funcao(self,x):
		return self.coeficiente_angular*x+self.coeficiente_linear
	def funcao_inversa(self,y):
		return -self.coeficiente_linear/self.coeficiente_angular+y/self.coeficiente_angular
	def somatorio(self,vetor):
		resposta=0
		for i in range(0,len(vetor)):
			resposta=resposta+vetor[i]
		return resposta
	def desvio_padrao(self,vetor):
		soma=0
		if(len(vetor)<=1):
			return -1
		media=self.somatorio(vetor)/len(vetor)
		for i in range(0,len(vetor)):
			soma=soma+(vetor[i]-media)*(vetor[i]-media)
		return math.sqrt(soma/(self.n-1))
	def residuos_normalizados(self):
		d=[]
		desvio=self.desvio_padrao(y)
		for i in range(0,len(y)):
			d.append((y[i]-self.funcao(x[i]))/desvio)
		return d