import numpy as np
import matplotlib.pyplot as plt 
n_puntos=1000
x=np.linspace(0.0,1.0,n_puntos)

u_inicial=np.exp(-(x-0.3)**2/0.01) #forma inicial de la onda

plt.plot(x,u_inicial)

delta_x=x[1]-x[0]
delta_t=0.0005
c=1.0
r=c*delta_t/delta_x

u_inicial[0]=0.0

u_inicial[n_puntos-1]=0.0


u_siguiente=np.zeros(n_puntos)
u_siguiente[0]=0.0
u_siguiente[n_puntos-1]=0.0

for i in range(1,n_puntos-1):
    u_siguiente[i]=u_inicial[i]+ (r**2/2.0)*(u_inicial[i+1]-2.0*u_inicial[i]+u_inicial[i-1])

u_pasado=u_inicial.copy()
u_presente=u_siguiente.copy()


plt.plot(x,u_pasado)
plt.plot(x,u_presente)



