import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from RegressaoLinearMultipla import RegressaoLinearMultipla
from GaussJordan import GaussJordan
x1=[0,0,1,2,0,1,2,2,1]
x2=[0,2,2,4,4,6,6,2,1]
y=[14,21,11,12,23,23,14,6,11]
regressao=RegressaoLinearMultipla(x1,x2,y)
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter3D(x1,x2,y,'red',linewidth=3.0)
x1=[]
x2=[]
y=[]
for i in range (0,600):
	for j in range (0,600):
		x1.append(i/100)
		x2.append(j/100)
		y.append(regressao.funcao(i/100,j/100))
ax.plot3D(x1,x2,y,'blue',linewidth=0.1)
ax.set_xlabel('X1 axis')
ax.set_ylabel('X2 axis')
ax.set_zlabel('Y axis')
plt.show()