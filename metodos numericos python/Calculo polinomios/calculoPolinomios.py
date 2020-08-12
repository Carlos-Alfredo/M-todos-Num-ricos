def funcao(valor,coeficientes):
	num_coef=len(coeficientes)
	x=[]
	x.append(1)
	resposta=coeficientes[0]
	for i in range(1,num_coef):
		x.append(x[i-1]*valor)
		resposta=resposta+x[i]*coeficientes[i]
	return resposta
x0=3.326530612244898
x1=3.4812727094176563
coeficientes=[-5,17.7,-11.7,2]
fx0=funcao(x0,coeficientes)
fx1=funcao(x1,coeficientes)
x=x1-fx1*(x1-x0)/(fx1-fx0)
print(x)