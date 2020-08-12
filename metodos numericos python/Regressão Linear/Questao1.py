from RegressaoLinear import RegressaoLinear
import matplotlib.pyplot as plt
import math

x=[0,2,4,6,9,11,12,15,17,19]
y=[5,6,7,6,9,8,7,10,12,12]
regressao=RegressaoLinear(x,y)
abcissas=[]
ordenadas=[]
for i in range(0,2000):
	abcissas.append(i/100)
	ordenadas.append(regressao.funcao(i/100))
plt.plot(abcissas,ordenadas)
plt.plot(x,y,'ro',linewidth=3.0)
plt.text(2.51,10,"R={}".format(regressao.r))
print(regressao.r)
print(regressao.residuos_normalizados())
plt.grid(True)
plt.show()