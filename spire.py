import random
from Quaternion import Quat


# floats for position
X = 0.0   
Y = 0.0
Z = 0.0

# floats for center of object
CenterX = 0.0 
CenterY = 0.0
CenterZ = 0.0

#floats for scale
xScale = 3
yScale = 1 #Y is up/down in besiege
zScale = 3 

#floats for three axis translation on each loop
xMoveRate = 0.0
yMoveRate = 0.0
zMoveRate = 0.0

# rotational angle, fixed/starting point
xRot = 0.0
yRot = 0.0
zRot = 0.0



# make a quaternion out of the rotation values
# pretty sure I got these right, X/Z are left/right & front/back, Y is spin around
# all rotation is done from object origin, not center, just be aware of that
blockRotation = Quat((xRot,yRot,zRot))  

# iterate the ID, every object in the XML doc needs a unique ID
 


def spirebuilder(id,scale,X,Y,Z):
    scale = scale * 0.1
    objID = id
    stupidLongString = ""
  #Actual XML here
    stupidLongString = str('''
<Object ID="''' + str(objID + 1) + '''" Prefab="9023">
<Position x= "''' + str(X) + '''" y="''' + str(Y) + '''" z="''' + str(Z) + '''"/>
<Rotation x="''' + str(blockRotation.q[0]) + '''" y="''' + str(blockRotation.q[1]) + '''" z="''' + str(blockRotation.q[2]) + '''" w="''' + str(blockRotation.q[3]) + '''" />
<Scale x="''' + str(6 * scale) +'''" y="''' + str(2*scale) +'''" z="''' + str(6 * scale) +'''" />
<Data>
<Color key="bmt-colour">
<R>0.3272059</R>
<G>0.4213492</G>
<B>0.5</B>
</Color>
<Boolean key="bmt-lel-enable-physics">False</Boolean>
</Data>
</Object>

<Object ID="''' + str(objID + 2) + '''" Prefab="9025">
<Position x= "''' + str(X) + '''" y="''' + str(Y+2 + (scale * 1.5)) + '''" z="''' + str(Z) + '''"/>
<Scale x="''' + str(2 * scale) +'''" y="''' + str(2 * scale) +'''" z="''' + str(2 * scale) +'''" />
<Data>
<Color key="bmt-colour">
<R>0.3272059</R>
<G>0.4213492</G>
<B>0.5</B>
</Color>
<Boolean key="bmt-lel-enable-physics">False</Boolean>
</Data>
</Object>

<Object ID="''' + str(objID + 3) + '''" Prefab="9024">
<Position x= "''' + str(X) + '''" y="''' + str(Y+6 + (scale * 1.5)) + '''" z="''' + str(Z) + '''"/>
<Scale x="''' + str(2 * scale) +'''" y="''' + str(6.8 * scale) +'''" z="''' + str(2 * scale) +'''" />
<Data>
<Color key="bmt-colour">
<R>0.3272059</R>
<G>0.4213492</G>
<B>0.5</B>
</Color>
<Boolean key="bmt-lel-enable-physics">False</Boolean>

</Data>
</Object>

<Object ID="''' + str(objID + 4) + '''" Prefab="9025">
<Position x= "''' + str(X) + '''" y="''' + str(Y + 12.5 + (scale * 1.5)) + '''" z="''' + str(Z) + '''"/>
<Scale x="''' + str(2 * scale) +'''" y="''' + str(2 * scale) +'''" z="''' + str(2 * scale) +'''" />
<Data>
<Color key="bmt-colour">
<R>0.3272059</R>
<G>0.4213492</G>
<B>0.5</B>
</Color>
<Boolean key="bmt-lel-enable-physics">False</Boolean>
</Data>
</Object>

<Object ID="''' + str(objID + 5) + '''" Prefab="9023">
<Position x= "''' + str(X) + '''" y="''' + str(Y + 16.5 + (scale)) + '''" z="''' + str(Z) + '''"/>
<Scale x="''' + str(6 * scale) +'''" y="''' + str(2 * scale) +'''" z="''' + str(6 * scale) +'''" />
<Data>
<Color key="bmt-colour">
<R>0.3254902</R>
<G>0.4196078</G>
<B>0.5019608</B>
</Color>
<String key="bmt-lel-name">Textured Cylinder</String>
<Boolean key="bmt-lel-enable-physics">False</Boolean>
</Data>
</Object>

<Object ID="''' + str(objID + 6) + '''" Prefab="9023">
<Position x= "''' + str(X) + '''" y="''' + str(Y + scale) + '''" z="''' + str(Z) + '''"/>
<Scale x="''' + str(scale) +'''" y="''' + str(scale * 35) +'''" z="''' + str(scale) +'''" />
<Data>
<Color key="bmt-colour">
<R>0.3254902</R>
<G>0.4196078</G>
<B>0.5019608</B>
</Color>
<String key="bmt-lel-name">Textured Cylinder</String>
<Boolean key="bmt-lel-enable-physics">False</Boolean>
</Data>
</Object>

''')

  #End Actual XML
    objID = objID + 1
    Y = Y + yScale
    return stupidLongString
