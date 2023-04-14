import roboticstoolbox as rtb
from math import pi
from spatialmath import SE3

# Create the robot (2R)
robot = rtb.models.DH.Planar2()

print(robot)

robot.plot(robot.qr)
input("Press enter")

############################################
# Forward kinematic
T1 = robot.fkine([0,0])
print(T1)

T2 = robot.fkine([pi/4,pi/4])
print(T2)

# robot.plot([pi/4,pi/4])

############################################
# Inverse Kinematic

solution1 = robot.ikine_LM(T1)
q1 = solution1[0]
print(q1)

solution2 = robot.ikine_LM(T2)
q2 = solution2[0]
print(q2)

T3 = SE3(0.7071, 1.707, 0)
solution3 = robot.ikine_LM(T3)
print(solution3)