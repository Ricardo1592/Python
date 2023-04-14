from spatialmath import *
from math import pi 

R=SO2(-pi/2)
R2=SO2(90, unit='deg')

a=[1,0]

a_1=R*a
a_2=R2*a

# print(a_2)

H1=SE2(pi/2)
H2=SE2(1,2)
H3=H1*H2  # Uma rotação de 90 graus e uma translação, é só multiplicar as matrizes

# print(H1)
# print(H2)
# print(H3)

a=[1,0]
a_1=H1*a
a_2=H2*a
a_3=H3*a

# print(a_1)
# print(a_2)
# print(a_3)

Rx=SO3.Rx(pi/2)
Ry=SO3.Ry(pi/2)
Rz=SO3.Rz(pi/2)
Rxyz=Rx*Ry*Rz
Rxzy=Rx*Rz*Ry

# print(Rx)
# print(Ry)
# print(Rz)
# print(Rxyz)
# print(Rxzy)

Tx=SE3.Tx(1)
Ty=SE3.Ty(2)
Tz=SE3.Tz(3)
Txyz=Tx*Ty*Tz

print(Tx)
print(Ty)
print(Tz)
print(Txyz)

a=[1,0,0]
# a_t=Ht*a