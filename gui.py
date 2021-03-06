# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(770, 721)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.layout_left = QtGui.QVBoxLayout()
        self.layout_left.setObjectName(_fromUtf8("layout_left"))
        self.layout_button = QtGui.QVBoxLayout()
        self.layout_button.setObjectName(_fromUtf8("layout_button"))
        self.button_start = QtGui.QPushButton(self.centralwidget)
        self.button_start.setObjectName(_fromUtf8("button_start"))
        self.layout_button.addWidget(self.button_start)
        self.button_camera_start = QtGui.QPushButton(self.centralwidget)
        self.button_camera_start.setObjectName(_fromUtf8("button_camera_start"))
        self.layout_button.addWidget(self.button_camera_start)
        self.button_camera_stop = QtGui.QPushButton(self.centralwidget)
        self.button_camera_stop.setObjectName(_fromUtf8("button_camera_stop"))
        self.layout_button.addWidget(self.button_camera_stop)
        self.button_camera_capture_image = QtGui.QPushButton(self.centralwidget)
        self.button_camera_capture_image.setObjectName(_fromUtf8("button_camera_capture_image"))
        self.layout_button.addWidget(self.button_camera_capture_image)
        self.button_calculate_camera_parameters = QtGui.QPushButton(self.centralwidget)
        self.button_calculate_camera_parameters.setObjectName(_fromUtf8("button_calculate_camera_parameters"))
        self.layout_button.addWidget(self.button_calculate_camera_parameters)
        self.button_correct_image = QtGui.QPushButton(self.centralwidget)
        self.button_correct_image.setObjectName(_fromUtf8("button_correct_image"))
        self.layout_button.addWidget(self.button_correct_image)
        self.button_reset_mirror = QtGui.QPushButton(self.centralwidget)
        self.button_reset_mirror.setObjectName(_fromUtf8("button_reset_mirror"))
        self.layout_button.addWidget(self.button_reset_mirror)
        self.button_test = QtGui.QPushButton(self.centralwidget)
        self.button_test.setObjectName(_fromUtf8("button_test"))
        self.layout_button.addWidget(self.button_test)
        self.label_geometry = QtGui.QLabel(self.centralwidget)
        self.label_geometry.setObjectName(_fromUtf8("label_geometry"))
        self.layout_button.addWidget(self.label_geometry)
        self.combobox_canal_horizontal = QtGui.QComboBox(self.centralwidget)
        self.combobox_canal_horizontal.setObjectName(_fromUtf8("combobox_canal_horizontal"))
        self.layout_button.addWidget(self.combobox_canal_horizontal)
        self.combobox_canal_vertical = QtGui.QComboBox(self.centralwidget)
        self.combobox_canal_vertical.setObjectName(_fromUtf8("combobox_canal_vertical"))
        self.layout_button.addWidget(self.combobox_canal_vertical)
        self.label_measure = QtGui.QLabel(self.centralwidget)
        self.label_measure.setObjectName(_fromUtf8("label_measure"))
        self.layout_button.addWidget(self.label_measure)
        self.combobox_canal_measure = QtGui.QComboBox(self.centralwidget)
        self.combobox_canal_measure.setObjectName(_fromUtf8("combobox_canal_measure"))
        self.layout_button.addWidget(self.combobox_canal_measure)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lable_distance = QtGui.QLabel(self.centralwidget)
        self.lable_distance.setObjectName(_fromUtf8("lable_distance"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lable_distance)
        self.lineedit_distance_to_object = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_distance_to_object.setObjectName(_fromUtf8("lineedit_distance_to_object"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineedit_distance_to_object)
        self.lineedit_distance_between_mirrors = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_distance_between_mirrors.setObjectName(_fromUtf8("lineedit_distance_between_mirrors"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineedit_distance_between_mirrors)
        self.label_distance_between_scanners = QtGui.QLabel(self.centralwidget)
        self.label_distance_between_scanners.setObjectName(_fromUtf8("label_distance_between_scanners"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_distance_between_scanners)
        self.layout_button.addLayout(self.formLayout)
        self.layout_left.addLayout(self.layout_button)
        self.layout_file = QtGui.QVBoxLayout()
        self.layout_file.setObjectName(_fromUtf8("layout_file"))
        self.button_folder_measurement = QtGui.QPushButton(self.centralwidget)
        self.button_folder_measurement.setObjectName(_fromUtf8("button_folder_measurement"))
        self.layout_file.addWidget(self.button_folder_measurement)
        self.lineedit_folder_measurement = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_folder_measurement.setObjectName(_fromUtf8("lineedit_folder_measurement"))
        self.layout_file.addWidget(self.lineedit_folder_measurement)
        self.label_file_name = QtGui.QLabel(self.centralwidget)
        self.label_file_name.setObjectName(_fromUtf8("label_file_name"))
        self.layout_file.addWidget(self.label_file_name)
        self.lineedit_file_name = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_file_name.setObjectName(_fromUtf8("lineedit_file_name"))
        self.layout_file.addWidget(self.lineedit_file_name)
        self.button_folder_image = QtGui.QPushButton(self.centralwidget)
        self.button_folder_image.setObjectName(_fromUtf8("button_folder_image"))
        self.layout_file.addWidget(self.button_folder_image)
        self.lineedit_folder_image = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_folder_image.setObjectName(_fromUtf8("lineedit_folder_image"))
        self.layout_file.addWidget(self.lineedit_folder_image)
        self.button_set_to_one_point = QtGui.QPushButton(self.centralwidget)
        self.button_set_to_one_point.setObjectName(_fromUtf8("button_set_to_one_point"))
        self.layout_file.addWidget(self.button_set_to_one_point)
        self.lineedit_one_point = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_one_point.setObjectName(_fromUtf8("lineedit_one_point"))
        self.layout_file.addWidget(self.lineedit_one_point)
        self.layout_left.addLayout(self.layout_file)
        self.horizontalLayout_2.addLayout(self.layout_left)
        self.layout_right = QtGui.QVBoxLayout()
        self.layout_right.setObjectName(_fromUtf8("layout_right"))
        self.layout_points = QtGui.QVBoxLayout()
        self.layout_points.setObjectName(_fromUtf8("layout_points"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.layout_points.addWidget(self.label)
        self.label_define_points = QtGui.QLabel(self.centralwidget)
        self.label_define_points.setObjectName(_fromUtf8("label_define_points"))
        self.layout_points.addWidget(self.label_define_points)
        self.radiobutton_mesh_points = QtGui.QRadioButton(self.centralwidget)
        self.radiobutton_mesh_points.setObjectName(_fromUtf8("radiobutton_mesh_points"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radiobutton_mesh_points)
        self.layout_points.addWidget(self.radiobutton_mesh_points)
        self.radiobutton_area_border = QtGui.QRadioButton(self.centralwidget)
        self.radiobutton_area_border.setObjectName(_fromUtf8("radiobutton_area_border"))
        self.buttonGroup.addButton(self.radiobutton_area_border)
        self.layout_points.addWidget(self.radiobutton_area_border)
        self.textedit_define_points = QtGui.QTextEdit(self.centralwidget)
        self.textedit_define_points.setObjectName(_fromUtf8("textedit_define_points"))
        self.layout_points.addWidget(self.textedit_define_points)
        self.form_mesh_properites = QtGui.QFormLayout()
        self.form_mesh_properites.setObjectName(_fromUtf8("form_mesh_properites"))
        self.maxAreaLabel = QtGui.QLabel(self.centralwidget)
        self.maxAreaLabel.setObjectName(_fromUtf8("maxAreaLabel"))
        self.form_mesh_properites.setWidget(0, QtGui.QFormLayout.LabelRole, self.maxAreaLabel)
        self.lineedit_mesh_max_area = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_mesh_max_area.setObjectName(_fromUtf8("lineedit_mesh_max_area"))
        self.form_mesh_properites.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineedit_mesh_max_area)
        self.minAngleLabel = QtGui.QLabel(self.centralwidget)
        self.minAngleLabel.setObjectName(_fromUtf8("minAngleLabel"))
        self.form_mesh_properites.setWidget(1, QtGui.QFormLayout.LabelRole, self.minAngleLabel)
        self.lineedit_mesh_min_angle = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_mesh_min_angle.setObjectName(_fromUtf8("lineedit_mesh_min_angle"))
        self.form_mesh_properites.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineedit_mesh_min_angle)
        self.layout_points.addLayout(self.form_mesh_properites)
        self.button_preview_mesh = QtGui.QPushButton(self.centralwidget)
        self.button_preview_mesh.setObjectName(_fromUtf8("button_preview_mesh"))
        self.layout_points.addWidget(self.button_preview_mesh)
        self.layout_right.addLayout(self.layout_points)
        self.horizontalLayout_2.addLayout(self.layout_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.button_start.setText(_translate("MainWindow", "Start Measurement", None))
        self.button_camera_start.setText(_translate("MainWindow", "Start Camera", None))
        self.button_camera_stop.setText(_translate("MainWindow", "Stop Camera", None))
        self.button_camera_capture_image.setText(_translate("MainWindow", "Capture Image", None))
        self.button_calculate_camera_parameters.setText(_translate("MainWindow", "Calculate Camera Parameters", None))
        self.button_correct_image.setText(_translate("MainWindow", "Correct Image", None))
        self.button_reset_mirror.setText(_translate("MainWindow", "Reset scanner", None))
        self.button_test.setText(_translate("MainWindow", "#TEST#", None))
        self.label_geometry.setText(_translate("MainWindow", "Scanner", None))
        self.label_measure.setText(_translate("MainWindow", "Velocity and Force", None))
        self.lable_distance.setText(_translate("MainWindow", "Distance to object [m]", None))
        self.label_distance_between_scanners.setText(_translate("MainWindow", "Distance between scanners [m]", None))
        self.button_folder_measurement.setText(_translate("MainWindow", "Select Folder For Measurement", None))
        self.label_file_name.setText(_translate("MainWindow", "File Name", None))
        self.button_folder_image.setText(_translate("MainWindow", "Select Folder For Images", None))
        self.button_set_to_one_point.setText(_translate("MainWindow", "Set Mirror To Point", None))
        self.label.setText(_translate("MainWindow", "Mesh", None))
        self.label_define_points.setText(_translate("MainWindow", "Define points", None))
        self.radiobutton_mesh_points.setText(_translate("MainWindow", "mesh points", None))
        self.radiobutton_area_border.setText(_translate("MainWindow", "area border", None))
        self.maxAreaLabel.setText(_translate("MainWindow", "Max Area", None))
        self.minAngleLabel.setText(_translate("MainWindow", "Min Angle", None))
        self.button_preview_mesh.setText(_translate("MainWindow", "Create/Preview mesh", None))

