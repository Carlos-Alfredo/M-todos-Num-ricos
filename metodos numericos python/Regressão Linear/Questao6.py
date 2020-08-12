import math
from RegressaoLinear import RegressaoLinear
import matplotlib.pyplot as plt
temperatura=[26.67,93.33,148.89,315.56]
viscosidade=[1.35,0.085,0.012,0.00075]
viscosidadeln=[]
for i in range(0,len(temperatura)):
	viscosidadeln.append(math.log(viscosidade[i]))
regressao=RegressaoLinear(temperatura,viscosidadeln)
print("ln(viscosidade)=",regressao.coeficiente_linear,"+Temperatura*",regressao.coeficiente_angular)
print("R^2=",regressao.r*regressao.r)
abcissas=[]
ordenadas=[]
for i in range(0,30000):
	abcissas.append(i/100)
	ordenadas.append(regressao.funcao(i/100))
plt.plot(abcissas,ordenadas)
plt.plot(temperatura,viscosidadeln,'ro',linewidth=3.0)
plt.text(2.51,10,"R^2={}".format(regressao.r*regressao.r))
plt.show()