import maya.cmds as cmds

# Generate a stone slab trail, 2 tree types, fences, and flowers. User is 
# encouraged to build their own trail using these assets.

# Stone slab trail: flat polygons for stones. 3 stones per generation.
cmds.polyCube(name="stepStones", depth=1, height=0.2, sx=2, sz=2)
ss_edges = ['stepStones.e[13]', 'stepStones.e[22]', 'stepStones.e[30]', 
            'stepStones.e[31]']
cmds.polyMoveEdge(ss_edges, ltz=0.1)
cmds.select("stepStones")
cmds.move(0.6, 1.6, xz=True)
cmds.rotate(-10, y=True)

# Tree 1: simple polys. Cylinder and 3 cones.
# Tree 2: simple polys. Cylinder and 3 spheres.
# Fences: simple polys. Cubes and bevel. 
# Flowers: simple polys. Cylinder and beveled cubes. Generates in clumps.

# Pyside GUI to interact with Maya.
    # Spinbox for asset scale.
    # Slider for asset rotation.