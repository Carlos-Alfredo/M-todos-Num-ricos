from RegressaoLinear import RegressaoLinear
import matplotlib.pyplot as plt
import math

x=[2.5,3.5,5,6,7.5,10,12.5,15,17.5,20]
y=[13,11,8.5,8.2,7,6.2,5.2,4.8,4.6,4.3]
ln_y=[]
for i in range(0,len(y)):
	ln_y.append(math.log(y[i]))

regressao=RegressaoLinear(x,ln_y)
ln_a=regressao.coeficiente_linear
b=regressao.coeficiente_angular
print("ln(a)=",ln_a,"\na=",math.exp(ln_a))
print("b=",b)
print("R=",regressao.r)
abcissas=[]
ordenadas=[]
for i in range(0,2000):
	abcissas.append(i/100)
	ordenadas.append(regressao.funcao(i/100))
plt.plot(x,ln_y,'ro')
plt.plot(abcissas,ordenadas)
plt.show()