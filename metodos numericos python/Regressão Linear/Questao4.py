from RegressaoCubica import RegressaoCubica
import matplotlib.pyplot as plt
x=[3,4,5,7,8,9,11,12]
y=[1.6,3.6,4.4,3.4,2.2,2.8,3.8,4.6]
regressao=RegressaoCubica(x,y)
solucao=regressao.solucao
abcissas=[]
ordenadas=[]
for i in range(0,2000):
	abcissas.append(i/100)
	ordenadas.append(regressao.funcao(i/100))
print("y=",solucao[0],"+x",solucao[1],"+x^2",solucao[2],"+x3",solucao[3])
plt.plot(abcissas,ordenadas)
plt.plot(x,y,'ro',linewidth=3.0)
plt.grid(True)
plt.show()