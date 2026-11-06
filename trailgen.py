import maya.cmds as cmds

# Generate a stone slab trail, 2 tree types, fences, and flowers. User is 
# encouraged to build their own trail using these assets.

# Stone slab trail: flat polygons for stones. 4 stones per generation.

class StepStones():
    
    def __init__(self):
        self.stone1_d = 1
        self.stone2_d = 1
        self.stone3_d = 1
        self.stone4_d = 1
        self.stone1_w = 1
        self.stone2_w = 1
        self.stone3_w = 1
        self.stone4_w = 1
        self.stone_h = 0.2
        self.stone_sx = 2
        self.stone_sz = 2
        self.ss_rotate = 0
        self.s1_r = -10
        self.s2_r = 8
        self.s3_r = 28
        self.s4_r = -21
    
    def create(self):
        group_objs = []
        group_objs.append(self.stone01())
        group_objs.append(self.stone02())
        group_objs.append(self.stone03())
        group_objs.append(self.stone04())
        cmds.group(group_objs, name="trail01")
        cmds.rotate(self.ss_rotate, y=True)

    def stone01(self):
        self.stone01_obj, self.stone01_node = cmds.polyCube(name="stone01", d=self.stone1_d, 
                                                            h=self.stone_h, w=self.stone1_w, 
                                                            sx=self.stone_sx, sz=self.stone_sz)
        s_edges = ['stone01.e[13]', 'stone01.e[22]', 'stone01.e[30]', 'stone01.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone01")
        cmds.move(0.6, 1.5, xz=True)
        cmds.rotate(self.s1_r, y=True)
        return self.stone01_obj

    def stone02(self):
        self.stone02_obj, self.stone02_node = cmds.polyCube(name="stone02", d=self.stone2_d, 
                                                            h=self.stone_h, w=self.stone2_w, 
                                                            sx=self.stone_sx, sz=self.stone_sz)
        s_edges = ['stone02.e[13]', 'stone02.e[22]', 'stone02.e[30]', 'stone02.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone02")
        cmds.move(-0.3, x=True)
        cmds.rotate(self.s2_r, y=True)
        return self.stone02_obj

    def stone03(self):
        self.stone03_obj, self.stone03_node = cmds.polyCube(name="stone03", d=self.stone3_d, 
                                                            h=self.stone_h, w=self.stone3_w, 
                                                            sx=self.stone_sx, sz=self.stone_sz)
        s_edges = ['stone03.e[13]', 'stone03.e[22]', 'stone03.e[30]', 'stone03.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone03")
        cmds.move(0.7,-1.4, xz=True)
        cmds.rotate(self.s3_r, y=True)
        return self.stone03_obj

    def stone04(self):
        self.stone04_obj, self.stone04_node = cmds.polyCube(name="stone04", d=self.stone4_d, 
                                                            h=self.stone_h, w=self.stone4_w, 
                                                            sx=self.stone_sx, sz=self.stone_sz)
        s_edges = ['stone04.e[13]', 'stone04.e[22]', 'stone04.e[30]', 'stone04.e[31]']
        cmds.polyMoveEdge(s_edges, ltz=0.1)
        cmds.select("stone04")
        cmds.move(-0.7,-2.4, xz=True)
        cmds.rotate(self.s4_r, y=True)
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
        self.lf_x = 1
        self.lf_y = 1
        self.lf_z = 1

    def create(self):
        group_objs = []
        group_objs.append(self.create_trunk())
        group_objs.append(self.create_leaves())
        cmds.group(group_objs, name="pine_tree01")
        cmds.scale(self.lf_x, self.lf_y, self.lf_z)
        #cmds.move(self.trunk_h, y=True)

    def create_trunk(self):
        self.trunk_obj, self.trunk_node = cmds.polyCylinder(name="trunk", h=self.trunk_h, 
                                                            r=self.trunk_r)
        cmds.xform(self.trunk_obj, translation=[0, self.trunk_h/2, 0])
        return self.trunk_obj

    def create_leaves(self):
        self.leaf01_obj, self.leaf01_node = cmds.polyCone(name="leaf01", h=self.leaf01_h, 
                                                          r=self.leaf01_r)
        cmds.xform(self.leaf01_obj, translation=[0, self.leaf01_h/2+self.trunk_h, 0])

        self.leaf02_obj, self.leaf02_node = cmds.polyCone(name="leaf02", h=self.leaf02_h, 
                                                          r=self.leaf02_r)
        cmds.xform(self.leaf02_obj, translation=[0, self.leaf02_h/2+self.trunk_h
                                            +(self.leaf01_h/2.6), 0])
        
        self.leaf03_obj, self.leaf03_node = cmds.polyCone(name="leaf03", h=self.leaf03_h, 
                                                          r=self.leaf03_r)
        cmds.xform(self.leaf03_obj, translation=[0, self.leaf03_h/2+self.trunk_h
                                            +(self.leaf01_h/2)+(self.leaf02_h)/2.9, 0])

        self.leaf_grp = cmds.group([self.leaf01_obj, self.leaf02_obj, self.leaf03_obj], 
                                   name="leaf_grp")
        return self.leaf_grp

# Tree 2: simple polys. Cylinders and 2 spheres.

class OakTree():

    def __init__(self):
        self.trunk_h = 2.3
        self.trunk_r = 0.3
        self.branch_h = 1
        self.branch_r = 0.2
        self.leaf01_r = 1.6
        self.leaf02_r = 1.2
        self.ot_rotate = 0
        self.lf_x = 1
        self.lf_y = 1
        self.lf_z = 1

    def create(self):
        group_objs = []
        group_objs.append(self.create_trunk())
        group_objs.append(self.create_leaves())
        cmds.group(group_objs, name="oak_tree01")
        cmds.rotate(self.ot_rotate, y=True)
        cmds.scale(self.lf_x, self.lf_y, self.lf_z)

    def create_trunk(self):
        self.trunk_obj, self.trunk_node = cmds.polyCylinder(name="trunk", h=self.trunk_h, 
                                                            r=self.trunk_r)
        cmds.xform(self.trunk_obj, translation=[0, self.trunk_h/2, 0])
        self.branch01_obj, self.branch01_node = cmds.polyCylinder(name="branch01", h=self.branch_h, 
                                                                  r=self.branch_r)
        cmds.xform(self.branch01_obj, translation=[-0.4, self.branch_h/2+self.trunk_h-0.3, 0], 
                   rotation=[0,0,33])
        self.branch02_obj, self.branch02_node = cmds.polyCylinder(name="branch02", h=self.branch_h, 
                                                                  r=self.branch_r)
        cmds.xform(self.branch02_obj, translation=[0.3, self.branch_h/2+self.trunk_h-0.5, 0], 
                   rotation=[0,0,-27])
        self.trunk_grp = cmds.group([self.trunk_obj, self.branch01_obj, self.branch02_obj], 
                                    name="trunk_grp")
        return self.trunk_grp

    def create_leaves(self):
        self.leaf01_obj, self.leaf01_node = cmds.polySphere(name="leaf01", r=self.leaf01_r)
        cmds.xform(self.leaf01_obj, translation=[-0.9, self.leaf01_r+self.trunk_h+0.5, 0])
        self.leaf02_obj, self.leaf02_node = cmds.polySphere(name="leaf02", r=self.leaf02_r)
        cmds.xform(self.leaf02_obj, translation=[1.3, self.leaf02_r+self.trunk_h-0.3, 0])
        self.leaf_grp = cmds.group([self.leaf01_obj, self.leaf02_obj], name="leaf_grp")
        return self.leaf_grp

# Fences: simple polys. Cubes and bevel. 

class Fence():

    def __init__(self):
        self.post_h = 1.3
        self.post_w = 0.3
        self.post_d = 0.2
        self.plank_h = 2.5
        self.plank_w = 0.2
        self.plank_d = 0.1

    def create(self):
        group_objs = []
        group_objs.append(self.create_posts())
        group_objs.append(self.create_planks())
        cmds.group(group_objs, name="fence01")

    def create_posts(self):
        self.post01_obj, self.post_node = cmds.polyCube(name="post01", h=self.post_h, w=self.post_w, 
                                                        d=self.post_d)
        p_edges = ['post01.e[6]', 'post01.e[7]']
        cmds.polyBevel( p_edges, segments=1, offset=0.1 )
        cmds.xform(self.post01_obj, translation=[0, self.post_h/2, 0])
        self.post02_obj, self.post_node = cmds.polyCube(name="post02", h=self.post_h, w=self.post_w, 
                                                        d=self.post_d)
        p_edges = ['post02.e[6]', 'post02.e[7]']
        cmds.polyBevel( p_edges, segments=1, offset=0.1 )
        cmds.xform(self.post02_obj, translation=[2, self.post_h/2, 0])
        self.posts_grp = cmds.group([self.post01_obj, self.post02_obj], name="posts_grp")
        return self.posts_grp

    def create_planks(self):
        self.plank01_obj, self.plank01_node = cmds.polyCube(name="plank01", h=self.plank_h, 
                                                            w=self.plank_w, d=self.plank_d)
        cmds.xform(self.plank01_obj, translation=[1, self.post_h/2+0.2, 0], rotation=[0,0,90])
        self.plank02_obj, self.plank02_node = cmds.polyCube(name="plank02", h=self.plank_h, 
                                                            w=self.plank_w, d=self.plank_d)
        cmds.xform(self.plank02_obj, translation=[1, self.post_h/2-0.2, 0], rotation=[0,0,90])
        self.plank_grp = cmds.group([self.plank01_obj, self.plank02_obj], name="plank_grp")
        return self.plank_grp
      

# Flowers: simple polys. Cylinder and beveled cubes.

class Flower():

    def __init__(self):
        self.stem_h = 0.4
        self.stem_r = 0.04
        self.petal_h = 0.15
        self.petal_w = 0.15
        self.petal_d = 0.15
        self.petal_sx = 2
        self.petal_sz = 2

    def create(self):
        group_objs = []
        group_objs.append(self.create_flower())
        cmds.group(group_objs, name="flower01")

    def create_flower(self):
        self.stem_obj, self.stem_node = cmds.polyCylinder(name="stem01", h=self.stem_h, r=self.stem_r)
        cmds.xform(self.stem_obj, translation=[0, self.stem_h/2, 0])
        self.petal_obj, self.petal_node = cmds.polyCube(name="petal01", h=self.petal_h, 
                                                        w=self.petal_w, d=self.petal_d, 
                                                        sx=self.petal_sx, sz=self.petal_sz)
        cmds.polySelect(self.petal_obj, edgeRing=1)
        cmds.polyExtrudeVertex(self.petal_obj, d=1, l=0.1, w=0.5)
        cmds.xform(self.petal_obj, translation=[0, self.petal_h/2+self.stem_h, 0])
        self.flower_grp = cmds.group([self.stem_obj, self.petal_obj], name="flower_grp")
        return self.flower_grp

# Pyside GUI to interact with Maya.
    # Spinbox for asset scale.
    # Slider for asset rotation.

import trailgen
import importlib
importlib.reload(trailgen)