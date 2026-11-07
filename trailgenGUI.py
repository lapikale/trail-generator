import importlib

from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui

import trailgen
importlib.reload(trailgen)
from trailgen import StepStones
from trailgen import PineTree
from trailgen import OakTree
from trailgen import Fence
from trailgen import Flower


def get_main_maya_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)

# //different tabs for different models

class TrailGenGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__(parent=get_main_maya_win())
        self.setWindowTitle("Trail Generator")
        self.setWindowFlag(QtCore.Qt.WindowType.Tool)
        self.create_layout()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.ss_tab = StepStonesGUI()
        self.pt_tab = PineTreeGUI()
        self.ot_tab = OakTreeGUI()
        self.fnc_tab = FenceGUI()
        self.flr_tab = FlowerGUI()

        self.tabs.addTab(self.ss_tab, "Stone Path")
        self.tabs.addTab(self.pt_tab, "Pine Tree")
        self.tabs.addTab(self.ot_tab, "Oak Tree")
        self.tabs.addTab(self.fnc_tab, "Fence")
        self.tabs.addTab(self.flr_tab, "Flower")

        self.main_lay.addWidget(self.tabs)

# StepStones:
# //individual stone rotate
# //individuale stone depth+width (scale)
# //group rotate
# //individual group boxes

class StepStonesGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ss_gen = StepStones()
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._group_boxes()
        self.create_btn = QtWidgets.QPushButton("Create Stone Path")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _group_boxes(self):
        self.grp_box = QtWidgets.QGroupBox("Group Editor")
        self.s1_box = QtWidgets.QGroupBox("Stone01 Editor")
        self.s2_box = QtWidgets.QGroupBox("Stone02 Editor")
        self.s3_box = QtWidgets.QGroupBox("Stone03 Editor")
        self.s4_box = QtWidgets.QGroupBox("Stone04 Editor")

        self.grp_lay = QtWidgets.QFormLayout()
        self.s1_lay = QtWidgets.QFormLayout()
        self.s2_lay = QtWidgets.QFormLayout()
        self.s3_lay = QtWidgets.QFormLayout()
        self.s4_lay = QtWidgets.QFormLayout()

        self.grp_box.setLayout(self.grp_lay)
        self.s1_box.setLayout(self.s1_lay)
        self.s2_box.setLayout(self.s2_lay)
        self.s3_box.setLayout(self.s3_lay)
        self.s4_box.setLayout(self.s4_lay)

        self._grp_edit()
        self._s1_edit()
        self._s2_edit()
        self._s3_edit()
        self._s4_edit()

        self.main_lay.addWidget(self.grp_box)
        self.main_lay.addWidget(self.s1_box)
        self.main_lay.addWidget(self.s2_box)
        self.main_lay.addWidget(self.s3_box)
        self.main_lay.addWidget(self.s4_box)

    def _grp_edit(self):
        self.grp_rotate_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.grp_rotate_slider.setMinimum(-180)
        self.grp_rotate_slider.setMaximum(180)
        self.grp_rotate_slider.setValue(0)
        self.grp_lay.addRow("Rotate", self.grp_rotate_slider)

    def _s1_edit(self):
        self.s1_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s1_r_slider.setMinimum(-180)
        self.s1_r_slider.setMaximum(180)
        self.s1_r_slider.setValue(-10)

        self.s1_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.s1_size_dspnbx.setValue(1)

        self.s1_lay.addRow("Rotate Stone01", self.s1_r_slider)
        self.s1_lay.addRow("Stone01 Size", self.s1_size_dspnbx)

    def _s2_edit(self):
        self.s2_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s2_r_slider.setMinimum(-180)
        self.s2_r_slider.setMaximum(180)
        self.s2_r_slider.setValue(8)

        self.s2_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.s2_size_dspnbx.setValue(1)

        self.s2_lay.addRow("Rotate Stone02", self.s2_r_slider)
        self.s2_lay.addRow("Stone02 Size", self.s2_size_dspnbx)

    def _s3_edit(self):
        self.s3_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s3_r_slider.setMinimum(-180)
        self.s3_r_slider.setMaximum(180)
        self.s3_r_slider.setValue(28)

        self.s3_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.s3_size_dspnbx.setValue(1)

        self.s3_lay.addRow("Rotate Stone03", self.s3_r_slider)
        self.s3_lay.addRow("Stone03 Size", self.s3_size_dspnbx)

    def _s4_edit(self):
        self.s4_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s4_r_slider.setMinimum(-180)
        self.s4_r_slider.setMaximum(180)
        self.s4_r_slider.setValue(-21)

        self.s4_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.s4_size_dspnbx.setValue(1)

        self.s4_lay.addRow("Rotate Stone04", self.s4_r_slider)
        self.s4_lay.addRow("Stone04 Size", self.s4_size_dspnbx)
    
    def create_connections(self):
        self.create_btn.clicked.connect(self.create)
    
    @QtCore.Slot()
    def create(self):
        self.ss_gen.ss_rotate = self.grp_rotate_slider.value()
        self.ss_gen.s1_r = self.s1_r_slider.value()
        self.ss_gen.s2_r = self.s2_r_slider.value()
        self.ss_gen.s3_r = self.s3_r_slider.value()
        self.ss_gen.s4_r = self.s4_r_slider.value()

        self.ss_gen.stone1_d = self.s1_size_dspnbx.value()
        self.ss_gen.stone1_w = self.s1_size_dspnbx.value()
        self.ss_gen.stone2_d = self.s2_size_dspnbx.value()
        self.ss_gen.stone2_w = self.s2_size_dspnbx.value()
        self.ss_gen.stone3_d = self.s3_size_dspnbx.value()
        self.ss_gen.stone3_w = self.s3_size_dspnbx.value()
        self.ss_gen.stone4_d = self.s4_size_dspnbx.value()
        self.ss_gen.stone4_w = self.s4_size_dspnbx.value()

        self.ss_gen.create()

# PineTree:
# //group scale
# //individual trunk height

class PineTreeGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.pt_gen = PineTree()
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QPushButton("Create Pine Tree")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self._trunk_edit()
        self._grp_edit()
        self.main_lay.addLayout(self.form_lay)

    def _trunk_edit(self):
        self.trunk_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.trunk_size_dspnbx.setValue(2)
        self.form_lay.addRow("Height", self.trunk_size_dspnbx)

    def _grp_edit(self):
        self.grp_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.grp_size_dspnbx.setValue(1)
        self.form_lay.addRow("Tree Size", self.grp_size_dspnbx)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.pt_gen.trunk_h = self.trunk_size_dspnbx.value()
        self.pt_gen.lf_x = self.grp_size_dspnbx.value()
        self.pt_gen.lf_y = self.grp_size_dspnbx.value()
        self.pt_gen.lf_z = self.grp_size_dspnbx.value()
        #make tree spawn at base
        self.pt_gen.create()

# OakTree:
# //group scale
# //group rotate
# //individual trunk height

class OakTreeGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ot_gen = OakTree()
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QPushButton("Create Oak Tree")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self._grp_edit()
        self._trunk_edit()
        self.main_lay.addLayout(self.form_lay)

    def _trunk_edit(self):
        self.trunk_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.trunk_size_dspnbx.setValue(2)
        self.form_lay.addRow("Height", self.trunk_size_dspnbx)

    def _grp_edit(self):
        self.grp_rotate_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.grp_rotate_slider.setMinimum(-180)
        self.grp_rotate_slider.setMaximum(180)
        self.grp_rotate_slider.setValue(0)
        self.form_lay.addRow("Rotate", self.grp_rotate_slider)

        self.grp_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.grp_size_dspnbx.setValue(1)
        self.form_lay.addRow("Tree Size", self.grp_size_dspnbx)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.ot_gen.ot_rotate = self.grp_rotate_slider.value()
        self.ot_gen.trunk_h = self.trunk_size_dspnbx.value()
        self.ot_gen.lf_x = self.grp_size_dspnbx.value()
        self.ot_gen.lf_y = self.grp_size_dspnbx.value()
        self.ot_gen.lf_z = self.grp_size_dspnbx.value()
        
        self.ot_gen.create()

# Fence:
# //individual plank rotation
# //group rotation
# group depth (length)

class FenceGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.fnc_gen = Fence()
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self._grp_edit()
        self._indv_plank()
        self.create_btn = QtWidgets.QPushButton("Create Fence")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self.main_lay.addLayout(self.form_lay)

    def _grp_edit(self):
        self.grp_rotate_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.grp_rotate_slider.setMinimum(-180)
        self.grp_rotate_slider.setMaximum(180)
        self.grp_rotate_slider.setValue(0)
        self.form_lay.addRow("Rotate", self.grp_rotate_slider)

    def _indv_plank(self):
        self.p1_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.p1_r_slider.setMinimum(80)
        self.p1_r_slider.setMaximum(100)
        self.p1_r_slider.setValue(90)
        self.form_lay.addRow("Rotate Plank01", self.p1_r_slider)

        self.p2_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.p2_r_slider.setMinimum(-10)
        self.p2_r_slider.setMaximum(10)
        self.p2_r_slider.setValue(0)
        self.form_lay.addRow("Rotate Plank02", self.p2_r_slider)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.fnc_gen.fnc_rotate = self.grp_rotate_slider.value()
        self.fnc_gen.p1_r = self.p1_r_slider.value()
        self.fnc_gen.p2_r = self.p2_r_slider.value()
            
        self.fnc_gen.create()

# Flower:
# //group scale
# //group rotate

class FlowerGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.flr_gen = Flower()
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self._grp_edit()
        self.create_btn = QtWidgets.QPushButton("Create Flower")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self.main_lay.addLayout(self.form_lay)

    def _grp_edit(self):
        self.grp_rotate_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.grp_rotate_slider.setMinimum(-180)
        self.grp_rotate_slider.setMaximum(180)
        self.grp_rotate_slider.setValue(0)
        self.form_lay.addRow("Rotate", self.grp_rotate_slider)

        self.grp_size_dspnbx = QtWidgets.QDoubleSpinBox()
        self.grp_size_dspnbx.setValue(1)
        self.form_lay.addRow("Flower Size", self.grp_size_dspnbx)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)
    
    @QtCore.Slot()
    def create(self):
        self.flr_gen.flr_rotate = self.grp_rotate_slider.value()
        self.flr_gen.flr_x = self.grp_size_dspnbx.value()
        self.flr_gen.flr_y = self.grp_size_dspnbx.value()
        self.flr_gen.flr_z = self.grp_size_dspnbx.value()
                
        self.flr_gen.create()