import numpy as np
import matplotlib.pyplot as plt

P=np.array([4,-1])
Q=np.array([-2,2])
C=np.array([0,0])
a=np.sqrt(20)
b=np.sqrt(5)
c=b*(1/a)
len=1000
B=np.linspace(-1,1,len)
x_AB1=np.zeros((2,len))
x_AB2=np.zeros((2,len))
e=np.sqrt(1-(c*c))
print e
for i in range(len):
   x=a*B[i]
   y1=b*(np.sqrt(1-(B[i]*B[i])))
   y2=-y1
   z1=C+np.array([x,y1])
   x_AB1[:,i]=z1.T
   z2=C+np.array([x,y2])
   x_AB2[:,i]=z2.T
   
plt.plot(x_AB1[0,:],x_AB1[1,:],'r')
plt.plot(x_AB2[0,:],x_AB2[1,:],'r')

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0.1),P[1]*(1+0.2),'P (4,-1)')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1+0.1),Q[1]*(1),'Q (-2,2)')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1+0.1),C[1]*(1),'C (0,0)')

plt.legend(loc='best')
plt.grid()
plt.show()

