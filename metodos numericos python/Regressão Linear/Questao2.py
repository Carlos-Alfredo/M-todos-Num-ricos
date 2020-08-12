from RegressaoLinear import RegressaoLinear
import matplotlib.pyplot as plt
import math

x=[2.5,3.5,5,6,7.5,10,12.5,15,17.5,20]
y=[13,11,8.5,8.2,7,6.2,5.2,4.8,4.6,4.3]
ln_x=[]
ln_y=[]
for i in range(0,len(x)):
	ln_x.append(math.log(x[i]))
for i in range(0,len(y)):
	ln_y.append(math.log(y[i]))

regressao=RegressaoLinear(ln_x,ln_y)
resultado=math.exp(regressao.funcao(math.log(9)))
print(resultado)
abcissas=[]
ordenadas=[]
for i in range (0,300):
	abcissas.append(i/100)
	ordenadas.append(regressao.funcao(i/100))
plt.plot(abcissas,ordenadas)
plt.plot(ln_x,ln_y,'ro')
plt.text(1,3,"R^2={}".format(regressao.r*regressao.r))
plt.show()