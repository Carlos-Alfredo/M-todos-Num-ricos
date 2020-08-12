import math
import matplotlib.pyplot as plt
from RegressaoLinear import RegressaoLinear
dia=[0,4,8,12,16,20]
quantidade=[67,84,98,125,149,185]
quantidade2=[]
for i in range (0,len(quantidade)):
	quantidade2.append(quantidade[i]*quantidade[i])
ln_quantidade=[]
for i in range(0,len(quantidade)):
	ln_quantidade.append(math.log(quantidade[i]))
regressaolinear=RegressaoLinear(dia,quantidade)
regressaoparabolica=RegressaoLinear(dia,quantidade2)
regressaoexponencial=RegressaoLinear(dia,ln_quantidade)

fig, graficos=plt.subplots(3)

abcissas=[]
ordenadas=[]
for i in range(0,2000):
	abcissas.append(i/100)
	ordenadas.append(regressaolinear.funcao(i/100))
graficos[0].plot(abcissas,ordenadas)
graficos[0].plot(regressaolinear.x,regressaolinear.y,'ro',linewidth=3.0)
graficos[0].text(2.51,55,"R^2={}".format(regressaolinear.r*regressaolinear.r))

abcissas=[]
ordenadas=[]
for i in range(0,2000):
	abcissas.append(i/100)
	ordenadas.append(regressaoparabolica.funcao(i/100))
graficos[1].plot(abcissas,ordenadas)
graficos[1].plot(regressaoparabolica.x,regressaoparabolica.y,'ro',linewidth=3.0)
graficos[1].text(2.51,10,"R^2={}".format(regressaoparabolica.r*regressaoparabolica.r))

abcissas=[]
ordenadas=[]
for i in range(0,2000):
	abcissas.append(i/100)
	ordenadas.append(regressaoexponencial.funcao(i/100))
graficos[2].plot(abcissas,ordenadas)
graficos[2].plot(regressaoexponencial.x,regressaoexponencial.y,'ro',linewidth=3.0)
graficos[2].text(4,4.16,"R^2={}".format(regressaoexponencial.r*regressaoexponencial.r))

print("Coeficiente Angular da exponencial=",regressaoexponencial.coeficiente_angular)
print("Coeficiente Linear da exponencial=",regressaoexponencial.coeficiente_linear)

plt.show()