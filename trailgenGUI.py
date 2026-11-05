import importlib

from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui

import trailgen
importlib.reload(trailgen)
from trailgen import StepStones


def get_main_maya_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)

# different tabs for different models

# StepStones:
# //individual stone rotate
# individuale stone depth+width (scale)
# //group rotate
# separator per stone

class StepStonesGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_main_maya_win())
        self.ss_gen = StepStones()
        self.setWindowTitle("Generate a Trail!")
        self.setWindowFlag(QtCore.Qt.WindowType.Tool)
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QPushButton("Create")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.grp_box = QtWidgets.QGroupBox("Rotate")
        self.form_lay = QtWidgets.QFormLayout()
        self._grp_edit()
        self._s1_edit()
        self._s2_edit()
        self._s3_edit()
        self._s4_edit()
        self.main_lay.addWidget(self.grp_box)
        self.main_lay.addLayout(self.form_lay)

    def _grp_edit(self):
        self.grp_rotate_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.grp_rotate_slider.setMinimum(-360)
        self.grp_rotate_slider.setMaximum(360)
        self.grp_rotate_slider.setValue(0)
        self.form_lay.addRow("Rotate", self.grp_rotate_slider)

    def _s1_edit(self):
        self.s1_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s1_r_slider.setMinimum(-360)
        self.s1_r_slider.setMaximum(360)
        self.s1_r_slider.setValue(-10)
        self.form_lay.addRow("Rotate Stone01", self.s1_r_slider)

    def _s2_edit(self):
        self.s2_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s2_r_slider.setMinimum(-360)
        self.s2_r_slider.setMaximum(360)
        self.s2_r_slider.setValue(8)
        self.form_lay.addRow("Rotate Stone02", self.s2_r_slider)

    def _s3_edit(self):
        self.s3_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s3_r_slider.setMinimum(-360)
        self.s3_r_slider.setMaximum(360)
        self.s3_r_slider.setValue(28)
        self.form_lay.addRow("Rotate Stone03", self.s3_r_slider)

    def _s4_edit(self):
        self.s4_r_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.s4_r_slider.setMinimum(-360)
        self.s4_r_slider.setMaximum(360)
        self.s4_r_slider.setValue(-21)
        self.form_lay.addRow("Rotate Stone04", self.s4_r_slider)
    
    def create_connections(self):
        self.create_btn.clicked.connect(self.create)
    
    @QtCore.Slot()
    def create(self):
        self.ss_gen.ss_rotate = self.grp_rotate_slider.value()
        self.ss_gen.s1_r = self.s1_r_slider.value()
        self.ss_gen.s2_r = self.s2_r_slider.value()
        self.ss_gen.s3_r = self.s3_r_slider.value()
        self.ss_gen.s4_r = self.s4_r_slider.value()
        self.ss_gen.create()

# Trees:
# toggle between type of tree
# group scale
# group rotate
# individual trunk height

# Fence:
# individual plank rotation
# group rotation
# group depth (length)

# Flower:
# group scale
# group rotate