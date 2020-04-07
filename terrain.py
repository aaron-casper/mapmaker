from Quaternion import Quat
import random

def terrainplacer(objID,X,Z,scale):
    xRot = 0
    yRot = random.randrange(0,360)
    zRot = 0
    blockRotation = Quat((xRot,yRot,zRot))
    stupidLongString = ('''		<Object ID="''' + str(objID) + '''" Prefab="2024">\n
    <Position x= "''' + str(X) + '''" y="0" z="''' + str(Z) + '''"/>\n
    <Rotation x="''' + str(blockRotation.q[0]) + '''" y="''' + str(blockRotation.q[1]) + '''" z="''' + str(blockRotation.q[2]) + '''" w="''' + str(blockRotation.q[3]) + '''" />
    <Scale x="2.5" y="''' + str(scale) + '''" z="2.5" />\n
    <Data>\n
    <Boolean key="bmt-Disable Texture">True</Boolean>\n
    <Boolean key="bmt-lel-enable-physics">False</Boolean>\n
    <Color key="bmt-colour">\n
    <R>0.5450981</R>\n
    <G>0.2705882</G>\n
    <B>0.07450981</B>\n
    </Color>
    </Data>\n
    </Object>\n''')
    return stupidLongString
    
