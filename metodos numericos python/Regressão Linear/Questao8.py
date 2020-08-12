import math
import matplotlib.pyplot as plt
from RegressaoLinear import RegressaoLinear
t=[4,8,12,16,20,24]
c=[1590,1320,1000,900,650,560]
c2=[]
for i in range (0,len(c)):
	c2.append(c[i]*c[i])
ln_c=[]
for i in range(0,len(c)):
	ln_c.append(math.log(c[i]))
regressaolinear=RegressaoLinear(t,c)
regressaoparabolica=RegressaoLinear(t,c2)
regressaoexponencial=RegressaoLinear(t,ln_c)

fig, graficos=plt.subplots(3)

abcissas=[]
ordenadas=[]
for i in range(0,2500):
	abcissas.append(i/100)
	ordenadas.append(regressaolinear.funcao(i/100))
graficos[0].plot(abcissas,ordenadas)
graficos[0].plot(regressaolinear.x,regressaolinear.y,'ro',linewidth=3.0)
graficos[0].text(3,700,"R^2={}".format(regressaolinear.r*regressaolinear.r))

abcissas=[]
ordenadas=[]
for i in range(0,2500):
	abcissas.append(i/100)
	ordenadas.append(regressaoparabolica.funcao(i/100))
graficos[1].plot(abcissas,ordenadas)
graficos[1].plot(regressaoparabolica.x,regressaoparabolica.y,'ro',linewidth=3.0)
graficos[1].text(3,600000,"R^2={}".format(regressaoparabolica.r*regressaoparabolica.r))

abcissas=[]
ordenadas=[]
for i in range(0,2500):
	abcissas.append(i/100)
	ordenadas.append(regressaoexponencial.funcao(i/100))
graficos[2].plot(abcissas,ordenadas)
graficos[2].plot(regressaoexponencial.x,regressaoexponencial.y,'ro',linewidth=3.0)
graficos[2].text(3,6.5,"R^2={}".format(regressaoexponencial.r*regressaoexponencial.r))

print("Coeficiente Angular da exponencial=",regressaoexponencial.coeficiente_angular)
print("Coeficiente Linear da exponencial=",regressaoexponencial.coeficiente_linear)
print("y(0)=",math.exp(regressaoexponencial.funcao(0)))
print("x(y=200)=",regressaoexponencial.funcao_inversa(math.log(200)))

plt.show()