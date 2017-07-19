import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n_puntos=300

x=np.linspace(0.0,30.0,n_puntos)
y=np.linspace(0.0,30.0,n_puntos)


matriz=np.zeros((n_puntos,n_puntos))

matriz[100,150]=-0.5

u_inicial=matriz #forma inicial de la onda

c=1.0
delta_x=x[1]-x[0]
delta_y=y[1]-y[0]

delta_t=0.05

gamma=(c* delta_t)/delta_x
beta=(c*delta_t)/delta_y


#condiciones de frontera fijas

rejilla_posicion= int((2*n_puntos)/3)

u_inicial[0]=0.0
u_inicial[n_puntos-1]=0.0
u_inicial[:,0]=0.0
u_inicial[:,n_puntos-1]=0.0


#u_inicial[rejilla_posicion]=0.0



u_siguiente=np.zeros((n_puntos,n_puntos))

u_siguiente[0]=0.0
u_siguiente[n_puntos-1]=0.0
u_siguiente[:,0]=0.0
u_siguiente[:,n_puntos-1]=0.0

#np.where((x<145)&(x>155))
#u_siguiente[rejilla_posicion]=0.0
  
   
for j in range(1,n_puntos-1):
    for i in range(1,n_puntos-1):
        u_siguiente[j,i]=0.5*( (gamma**2)*(u_inicial[j,i+1]-2.0*u_inicial[j,i]+u_inicial[j,i-1])+(beta**2)*(u_inicial[j+1,i]-2.0*u_inicial[j,i]+u_inicial[j-1,i])+2.0*u_inicial[j,i] )

u_pasado=u_inicial.copy()
u_presente=u_siguiente.copy()



n_tiempo=400

imagelist=[]
imagelist.append(u_inicial)


for l in range(n_tiempo):
    
    for i in range(1,n_puntos-1):
        for j in range(1,n_puntos-1):
            
            u_siguiente[j,i]=2.0*(1-gamma**2-beta**2)*u_presente[j,i]-u_pasado[j,i]+(gamma**2)*(u_presente[j,i+1]+u_presente[j,i-1])+(beta**2)*(u_presente[j+1,i]+u_presente[j-1,i])
            
    u_pasado=u_presente.copy()
    u_presente=u_siguiente.copy()
    
    if(l%10==0):
        imagelist.append(u_presente)

    if(l==30):
        
        plt.imshow(u_presente,cmap='gray')
        plt.savefig('30.png')
        plt.close()
        
    if(l==(n_tiempo-1)):
        
        plt.imshow(u_presente)
        plt.savefig('60.png')
        plt.close()

        



fig=plt.figure()

im=plt.imshow(imagelist[0],cmap=plt.get_cmap('jet'))

def updatefig(i):
    
    im.set_array(imagelist[i])
    
    return [im]

ani=animation.FuncAnimation(fig,updatefig,frames=range(20),interval=50,blit=True)

plt.show()
writer = ImageMagickFileWriter()
ani.save('onda.mp4')


