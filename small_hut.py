#TODO: convert this to a module, need to maintain relative X/Y for all parts to make building stay together
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
 


def hutbuilder(objID,X,Y):
    stupidLongString = ('''<Object ID="''' + str(objID + 1) + '''" Prefab="7000">
                        <Position x="''' + str(X - 12.2) + '''" y="0.699" z="''' + str(Y - 1) + '''" />
			<Scale x="5.984" y="9" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 2) + '''" Prefab="7000">
                        <Position x="''' + str(X - 0.949) + '''" y="0.699" z="''' + str(Y + 14.5) + '''" />
			<Scale x="5.984" y="7.56" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 3) + '''" Prefab="7000">
                    <Position x="''' + str(X - 12.3) + '''" y="0.699" z="''' + str(Y + 14.5) + '''" />
			<Scale x="5.44" y="7.56" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 4) + '''" Prefab="7000">
                        <Position x="''' + str(X - 6.5) + '''" y="8.2" z="''' + str(Y + 14.5) + '''" />
			<Scale x="17" y="1.5" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 5) + '''" Prefab="9028">
                        <Position x="''' + str(X - 12) + '''" y="11.5" z="''' + str(Y + 6.25) + '''" />
			<Rotation x="2.175935E-14" y="0.3827946" z="-1.247303E-07" w="0.9238335" />
			<Scale x="16" y="3" z="16" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2666667</R>
					<G>0</G>
					<B>0</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 6) + '''" Prefab="9028">
			
			<Position x="''' + str(X - 6.392) + '''" y="11.5" z="''' + str(Y + 11.904) + '''" />
			<Rotation x="-9.95136E-14" y="-0.9239255" z="3.01053E-07" w="-0.3825723" />
			<Scale x="16" y="3" z="16" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2666667</R>
					<G>0</G>
					<B>0</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
				<String key="bmt-lel-name">Pyramid Corner</String>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 7) + '''" Prefab="9028">
		        <Position x="''' + str(X - 0.7) + '''" y="11.5" z="''' + str(Y + 6.3) + '''" />
			<Rotation x="-7.603229E-15" y="0.9238335" z="-3.010234E-07" w="-0.3827946" />
			<Scale x="16" y="3" z="16" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2666667</R>
					<G>0</G>
					<B>0</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
				<String key="bmt-lel-name">Pyramid Corner</String>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 8) + '''" Prefab="9028">
                        <Position x="''' + str(X - 6.392) + '''" y="11.5" z="''' + str(Y + 0.75) + '''" />
			<Rotation x="-3.745494E-13" y="-0.3825723" z="1.246581E-07" w="0.9239255" />
			<Scale x="16" y="3" z="16" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2666667</R>
					<G>0</G>
					<B>0</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
				<String key="bmt-lel-name">Pyramid Corner</String>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 9) + '''" Prefab="7000">
                        <Position x="''' + str(X - 6.6) + '''" y="0.699" z="''' + str(Y - 1.5) + '''" />
			<Scale x="4.896" y="9" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 10) + '''" Prefab="7000">
		        <Position x="''' + str(X - 15.6) + '''" y="0.699" z="''' + str(Y + 12.2) + '''" />
			<Rotation x="1.130467E-14" y="0.7071068" z="-2.304047E-07" w="0.7071068" />
			<Scale x="5.100005" y="10" z="1.000001" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 11) + '''" Prefab="7000">
                        <Position x="''' + str(X - 15.6) + '''" y="0.699" z="''' + str(Y + 6.6) + '''" />
			<Rotation x="1.130467E-14" y="0.7071068" z="-2.304047E-07" w="0.7071068" />
			<Scale x="5.610009" y="10" z="1.000002" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 12) + '''" Prefab="7000">
			<Position x="''' + str(X - 15.6) + '''" y="0.699" z="''' + str(Y + 0.9) + '''" />
                        <Rotation x="1.130467E-14" y="0.7071068" z="-2.304047E-07" w="0.7071068" />
			<Scale x="5.100005" y="10" z="1.000001" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 13) + '''" Prefab="7000">
                        <Position x="''' + str(X + 2.6) + '''" y="0.699" z="''' + str(Y + 0.9) + '''" />
			<Rotation x="1.130467E-14" y="0.7071068" z="-2.304047E-07" w="0.7071068" />
			<Scale x="5.100005" y="10" z="1.000001" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 14) + '''" Prefab="7000">
                        <Position x="''' + str(X + 2.6) + '''" y="0.699" z="''' + str(Y + 6.6) + '''" />
			<Rotation x="1.130467E-14" y="0.7071068" z="-2.304047E-07" w="0.7071068" />
			<Scale x="5.610009" y="10" z="1.000002" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 15) + '''" Prefab="7000">
                        <Position x="''' + str(X + 2.6) + '''" y="0.699" z="''' + str(Y + 12.2) + '''" />
			<Rotation x="1.130467E-14" y="0.7071068" z="-2.304047E-07" w="0.7071068" />
			<Scale x="5.100005" y="10" z="1.000001" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 16) + '''" Prefab="7000">
                        <Position x="''' + str(X - 6.5) + '''" y="9.7" z="''' + str(Y + 6.5) + '''" />
			<Scale x="16.9" y="1" z="16.9" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 17) + '''" Prefab="7000">
                        <Position x="''' + str(X - 0.9) + '''" y="0.699" z="''' + str(Y - 1.5) + '''" />
			<Scale x="5.984" y="9" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 18) + '''" Prefab="2024">
                        <Position x="''' + str(X - 11) + '''" y="0" z="''' + str(Y + 5.9) + '''" />
			<Scale x="1" y="0.07986001" z="1" />
			<Data>
				<Color key="bmt-colour">
					<R>0.4705882</R>
					<G>0.8078431</G>
					<B>0.003921569</B>
				</Color>
			</Data>
		</Object>
		<Object ID="''' + str(objID + 19) + '''" Prefab="7000">
                        <Position x="''' + str(X - 6.5) + '''" y="-0.4" z="''' + str(Y + 6.5) + '''" />
			<Scale x="20" y="1" z="20" />
			<Data>
				<Color key="bmt-colour">
					<R>0.2</R>
					<G>0.2</G>
					<B>0.2</B>
				</Color>
				<Boolean key="bmt-Disable Texture">True</Boolean>
				<Boolean key="bmt-lel-enable-physics">False</Boolean>
			</Data>
		</Object>''')
    return stupidLongString
