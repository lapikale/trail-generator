import maya.cmds as cmds

# Generate a stone slab trail, 2 tree types, fences, and flowers. User is 
# encouraged to build their own trail using these assets.

# Stone slab trail: flat polygons for stones. 3 stones per generation.

class StepStones():
    
    def __init__(self):
        self.stone_d = 1
        self.stone_h = 0.2
        self.stone_sx = 2
        self.stone_sz = 2
    
    def create(self):
        group_objs = []
        group_objs.append(self.stone01())
        group_objs.append(self.stone02())
        group_objs.append(self.stone03())
        group_objs.append(self.stone04())
        cmds.group(group_objs, name="trail")

    def stone01(self):
        self.stone01_obj, self.stone01_node = cmds.polyCube(name="stone01", d=self.stone_d, 
                                                            h=self.stone_h, sx=self.stone_sx, 
                                                            sz=self.stone_sz)
        s_edges = ['stone01.e[13]', 'stone01.e[22]', 'stone01.e[30]', 'stone01.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone01")
        cmds.move(0.6, 1.5, xz=True)
        cmds.rotate(-10, y=True)
        return self.stone01_obj

    def stone02(self):
        self.stone02_obj, self.stone02_node = cmds.polyCube(name="stone02", d=self.stone_d, 
                                                            h=self.stone_h, sx=self.stone_sx, 
                                                            sz=self.stone_sz)
        s_edges = ['stone02.e[13]', 'stone02.e[22]', 'stone02.e[30]', 'stone02.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone02")
        cmds.move(-0.3, x=True)
        cmds.rotate(8, y=True)
        return self.stone02_obj

    def stone03(self):
        self.stone03_obj, self.stone03_node = cmds.polyCube(name="stone03", d=self.stone_d, 
                                                            h=self.stone_h, sx=self.stone_sx, 
                                                            sz=self.stone_sz)
        s_edges = ['stone03.e[13]', 'stone03.e[22]', 'stone03.e[30]', 'stone03.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone03")
        cmds.move(0.7,-1.4, xz=True)
        cmds.rotate(28, y=True)
        return self.stone03_obj

    def stone04(self):
        self.stone04_obj, self.stone04_node = cmds.polyCube(name="stone04", d=self.stone_d, 
                                                            h=self.stone_h, sx=self.stone_sx, 
                                                            sz=self.stone_sz)
        s_edges = ['stone04.e[13]', 'stone04.e[22]', 'stone04.e[30]', 'stone04.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone04")
        cmds.move(-0.7,-2.4, xz=True)
        cmds.rotate(-21, y=True)
        return self.stone04_obj

# Tree 1: simple polys. Cylinder and 3 cones.

class PineTree():

    def __init__(self):
        self.trunk_h = 2
        self.trunk_r = 0.3
        self.leaf01_h = 2.7
        self.leaf01_r = 1.7
        self.leaf02_h = 2.3
        self.leaf02_r = 1.3
        self.leaf03_h = 1.8
        self.leaf03_r = 0.9

    def create(self):
        group_objs = []
        group_objs.append(self.trunk_obj())
        group_objs.append(self.leaf01_obj())
        group_objs.append(self.leaf02_obj())
        group_objs.append(self.leaf03_obj())
        cmds.group(group_objs, name="pine_tree")

    def create_trunk(self):
        self.trunk_obj, self.trunk_node = cmds.polyCylinder(name="trunk", h=self.trunk_h, r=self.trunk_r)
        cmds.xform(self.trunk_obj, translation=[0, self.trunk_h/2, 0])
        return self.trunk_obj

    def create_leaves(self):
        self.leaf01_obj, self.leaf01_node = cmds.polyCone(name="leaf01", h=self.leaf01_h, r=self.leaf01_r)
        cmds.xform(self.leaf01_obj, translation=[0, self.leaf01_h/2+self.trunk_h, 0])

        self.leaf02_obj, self.leaf02_node = cmds.polyCone(name="leaf02", h=self.leaf02_h, r=self.leaf02_r)
        cmds.xform(self.leaf02_obj, translation=[0, self.leaf02_h/2+self.trunk_h
                                            +(self.leaf01_h/2.6), 0])
        
        self.leaf03_obj, self.leaf03_node = cmds.polyCone(name="leaf03", h=self.leaf03_h, r=self.leaf03_r)
        cmds.xform(self.leaf03_obj, translation=[0, self.leaf03_h/2+self.trunk_h
                                            +(self.leaf01_h/2)+(self.leaf02_h)/2.9, 0])

        self.leaf_grp = cmds.group([self.leaf01_obj, self.leaf02_obj, self.leaf03_obj], 
                                   name="leaf_grp")
        return self.leaf_grp

# Tree 2: simple polys. Cylinder and 3 spheres.

trunk_h = 2.3
trunk_r = 0.3
branch_h = 1
branch_r = 0.2
leaf01_r = 1.6
leaf02_r = 1.2


trunk_obj, trunk_node = cmds.polyCylinder(name="trunk", h=trunk_h, r=trunk_r)
cmds.xform(trunk_obj, translation=[0, trunk_h/2, 0])
branch01_obj, branch01_node = cmds.polyCylinder(name="branch01", h=branch_h, r=branch_r)
cmds.xform(branch01_obj, translation=[-0.4, branch_h/2+trunk_h-0.3, 0], rotation=[0,0,33])
branch02_obj, branch02_node = cmds.polyCylinder(name="branch02", h=branch_h, r=branch_r)
cmds.xform(branch02_obj, translation=[0.3, branch_h/2+trunk_h-0.5, 0], rotation=[0,0,-27])

leaf01_obj, leaf01_node = cmds.polySphere(name="leaf01", r=leaf01_r)
cmds.xform(leaf01_obj, translation=[-0.9, leaf01_r+trunk_h+0.5, 0])
leaf02_obj, leaf02_node = cmds.polySphere(name="leaf02", r=leaf02_r)
cmds.xform(leaf02_obj, translation=[1.3, leaf02_r+trunk_h-0.3, 0])

trunk_grp = cmds.group([trunk_obj, branch01_obj, branch02_obj], name="trunk_grp")
leaf_grp = cmds.group([leaf01_obj, leaf02_obj], name="leaf_grp")
oak_grp = cmds.group([trunk_grp, leaf_grp], name="oak_tree01")

# Fences: simple polys. Cubes and bevel. 
# Flowers: simple polys. Cylinder and beveled cubes. Generates in clumps.

# Pyside GUI to interact with Maya.
    # Spinbox for asset scale.
    # Slider for asset rotation.

import trailgen
import importlib
importlib.reload(trailgen)

trail01 = trailgen.StepStones()
tree01 = trailgen.PineTree()
trail01.create()
tree01.create()