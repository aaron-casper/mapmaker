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
 


def bricklayer(id,rowLength,wallHeight,X,Y,Z):
    X = X - (rowLength * 0.5)
    objID = id
    leftRight = 0
    heightCompleted = 0
    stupidLongString = ""
    while heightCompleted < wallHeight:

        i = 0

        while i < rowLength:
            noise = random.randrange(1,10,1)
            noise = noise * 0.1
            #print(noise)
            objID = objID + 1
  #Actual XML here
            stupidLongString = stupidLongString + str('''		<Object ID="''' + str(objID) + '''" Prefab="7000">
<Position x= "''' + str(X) + '''" y="''' + str(Y) + '''" z="''' + str(Z + noise) + '''"/>
<Rotation x="''' + str(blockRotation.q[0]) + '''" y="''' + str(blockRotation.q[1]) + '''" z="''' + str(blockRotation.q[2]) + '''" w="''' + str(blockRotation.q[3]) + '''" />
<Scale x="''' + str(xScale) + '''" y="''' + str(yScale) + '''" z="''' + str(zScale) + '''"/>
<Data>
<Boolean key="bmt-Disable Texture">True</Boolean>
<Boolean key="bmt-lel-enable-physics">True</Boolean>
<Single key="bmt-friction">0.6</Single>
</Data>
</Object>''')
  #End Actual XML
            objID = objID + 1
            X = X + xScale
            i = i + 1
  #counting rows, offsetting each row, like bricks of course
        heightCompleted = heightCompleted + 1
        Y = Y + yScale
        if int(Y) % 2 == 0:
            X = X - (int(rowLength * xScale) + int(xScale * 0.5))
        else:
            X = X - (int(rowLength * xScale) - int(xScale * 0.5))
    return stupidLongString
