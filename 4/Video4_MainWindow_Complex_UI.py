# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow_Complex_UI_css_FINAL_entire_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 391)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget_1 = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_1.setFont(font)
        self.tabWidget_1.setAcceptDrops(True)
        self.tabWidget_1.setObjectName("tabWidget_1")
        self.tab_widgets_1 = QtWidgets.QWidget()
        self.tab_widgets_1.setToolTip("")
        self.tab_widgets_1.setStatusTip("")
        self.tab_widgets_1.setObjectName("tab_widgets_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_widgets_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_tab_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab_1.setObjectName("verticalLayout_tab_1")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_widgets_1)
        self.tabWidget_2.setAccessibleName("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_tree = QtWidgets.QWidget()
        self.tab_tree.setStatusTip("")
        self.tab_tree.setObjectName("tab_tree")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_tree)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_tree)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tabWidget_2.addTab(self.tab_tree, "")
        self.tab_calendar = QtWidgets.QWidget()
        self.tab_calendar.setStatusTip("")
        self.tab_calendar.setObjectName("tab_calendar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_calendar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_calendar)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_3.addWidget(self.dateEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_calendar)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.tabWidget_2.addTab(self.tab_calendar, "")
        self.verticalLayout_tab_1.addWidget(self.tabWidget_2)
        self.verticalLayout.addLayout(self.verticalLayout_tab_1)
        self.tabWidget_1.addTab(self.tab_widgets_1, "")
        self.tab_widgets_2 = QtWidgets.QWidget()
        self.tab_widgets_2.setToolTip("")
        self.tab_widgets_2.setStatusTip("")
        self.tab_widgets_2.setObjectName("tab_widgets_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_widgets_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 140, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_widgets_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_widgets_2)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 114, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_start = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_start.setChecked(True)
        self.radioButton_start.setObjectName("radioButton_start")
        self.verticalLayout_4.addWidget(self.radioButton_start)
        self.radioButton_stop = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_stop.setObjectName("radioButton_stop")
        self.verticalLayout_4.addWidget(self.radioButton_stop)
        self.radioButton_reset = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_reset.setObjectName("radioButton_reset")
        self.verticalLayout_4.addWidget(self.radioButton_reset)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_widgets_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 61, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.dial = QtWidgets.QDial(self.verticalLayoutWidget)
        self.dial.setObjectName("dial")
        self.verticalLayout_5.addWidget(self.dial)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 20, 91, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_6.addWidget(self.lcdNumber)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_widgets_2)
        self.fontComboBox.setObjectName("fontComboBox")
        self.verticalLayout_7.addWidget(self.fontComboBox)
        self.label = QtWidgets.QLabel(self.tab_widgets_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.tabWidget_1.addTab(self.tab_widgets_2, "")
        self.tab_drag_drop = QtWidgets.QWidget()
        self.tab_drag_drop.setAcceptDrops(False)
        self.tab_drag_drop.setObjectName("tab_drag_drop")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_drag_drop)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_drag_drop)
        self.lineEdit.setMinimumSize(QtCore.QSize(135, 0))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.tab_drag_drop)
        self.comboBox.setMinimumSize(QtCore.QSize(141, 0))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.tab_drag_drop)
        self.pushButton.setMinimumSize(QtCore.QSize(161, 0))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.tab_drag_drop)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_3.addWidget(self.listWidget, 1, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_drag_drop)
        self.listWidget_2.setDragEnabled(True)
        self.listWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 1, 1, 1)
        self.tabWidget_1.addTab(self.tab_drag_drop, "")
        self.tab_gl = QtWidgets.QWidget()
        self.tab_gl.setObjectName("tab_gl")
        self.frame_gl = QtWidgets.QFrame(self.tab_gl)
        self.frame_gl.setGeometry(QtCore.QRect(120, 10, 300, 300))
        self.frame_gl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gl.setObjectName("frame_gl")
        self.tabWidget_1.addTab(self.tab_gl, "")
        self.tab_network = QtWidgets.QWidget()
        self.tab_network.setObjectName("tab_network")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_network)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_network)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textEdit_client_1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_client_1.setObjectName("textEdit_client_1")
        self.verticalLayout_8.addWidget(self.textEdit_client_1)
        self.lineEdit_client_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_client_1.setObjectName("lineEdit_client_1")
        self.verticalLayout_8.addWidget(self.lineEdit_client_1)
        self.button_client_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_client_1.setObjectName("button_client_1")
        self.verticalLayout_8.addWidget(self.button_client_1)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_start_server = QtWidgets.QPushButton(self.tab_network)
        self.button_start_server.setObjectName("button_start_server")
        self.horizontalLayout_4.addWidget(self.button_start_server)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_network)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textEdit_client_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_client_2.setObjectName("textEdit_client_2")
        self.verticalLayout_9.addWidget(self.textEdit_client_2)
        self.lineEdit_client_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_client_2.setObjectName("lineEdit_client_2")
        self.verticalLayout_9.addWidget(self.lineEdit_client_2)
        self.button_client_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.button_client_2.setObjectName("button_client_2")
        self.verticalLayout_9.addWidget(self.button_client_2)
        self.horizontalLayout_5.addWidget(self.groupBox_4)
        self.tabWidget_1.addTab(self.tab_network, "")
        self.tab_SQL = QtWidgets.QWidget()
        self.tab_SQL.setObjectName("tab_SQL")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_SQL)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.button_SQL_view_data = QtWidgets.QPushButton(self.tab_SQL)
        self.button_SQL_view_data.setObjectName("button_SQL_view_data")
        self.verticalLayout_11.addWidget(self.button_SQL_view_data)
        self.button_SQL_add = QtWidgets.QPushButton(self.tab_SQL)
        self.button_SQL_add.setObjectName("button_SQL_add")
        self.verticalLayout_11.addWidget(self.button_SQL_add)
        self.button_SQL_delete = QtWidgets.QPushButton(self.tab_SQL)
        self.button_SQL_delete.setObjectName("button_SQL_delete")
        self.verticalLayout_11.addWidget(self.button_SQL_delete)
        self.button_SQL_create_db = QtWidgets.QPushButton(self.tab_SQL)
        self.button_SQL_create_db.setObjectName("button_SQL_create_db")
        self.verticalLayout_11.addWidget(self.button_SQL_create_db)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.tableView = QtWidgets.QTableView(self.tab_SQL)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_3.addWidget(self.tableView)
        self.tabWidget_1.addTab(self.tab_SQL, "")
        self.tab_animation = QtWidgets.QWidget()
        self.tab_animation.setObjectName("tab_animation")
        self.button_start_animation = QtWidgets.QPushButton(self.tab_animation)
        self.button_start_animation.setGeometry(QtCore.QRect(10, 290, 101, 23))
        self.button_start_animation.setObjectName("button_start_animation")
        self.frame = QtWidgets.QFrame(self.tab_animation)
        self.frame.setGeometry(QtCore.QRect(10, 10, 100, 100))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setObjectName("frame")
        self.lcdNumber_animation = QtWidgets.QLCDNumber(self.tab_animation)
        self.lcdNumber_animation.setGeometry(QtCore.QRect(420, 10, 89, 78))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 170, 255))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lcdNumber_animation.setPalette(palette)
        self.lcdNumber_animation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber_animation.setDigitCount(3)
        self.lcdNumber_animation.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_animation.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_animation.setObjectName("lcdNumber_animation")
        self.button_stop_animation = QtWidgets.QPushButton(self.tab_animation)
        self.button_stop_animation.setGeometry(QtCore.QRect(120, 290, 101, 23))
        self.button_stop_animation.setObjectName("button_stop_animation")
        self.toolButton = QtWidgets.QToolButton(self.tab_animation)
        self.toolButton.setGeometry(QtCore.QRect(340, 20, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.tabWidget_1.addTab(self.tab_animation, "")
        self.tab_CSS = QtWidgets.QWidget()
        self.tab_CSS.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 \n"
"rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 0, 127)\n"
"}\n"
"QPushButton#pushButton_4{\n"
"background-color: rgb(255, 0, 255)\n"
"}")
        self.tab_CSS.setObjectName("tab_CSS")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_CSS)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_CSS)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_CSS)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_CSS)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 60, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget_1.addTab(self.tab_CSS, "")
        self.verticalLayout_10.addWidget(self.tabWidget_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_1.setCurrentIndex(7)
        self.tabWidget_2.setCurrentIndex(0)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        self.fontComboBox.activated['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget_2, self.treeWidget)
        MainWindow.setTabOrder(self.treeWidget, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.calendarWidget)
        MainWindow.setTabOrder(self.calendarWidget, self.radioButton_start)
        MainWindow.setTabOrder(self.radioButton_start, self.radioButton_stop)
        MainWindow.setTabOrder(self.radioButton_stop, self.radioButton_reset)
        MainWindow.setTabOrder(self.radioButton_reset, self.dial)
        MainWindow.setTabOrder(self.dial, self.fontComboBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Header 1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Item1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Subitem1"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_tree), _translate("MainWindow", "Tree"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_calendar), _translate("MainWindow", "Calendar"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_widgets_1), _translate("MainWindow", "Widgets 1"))
        self.groupBox.setTitle(_translate("MainWindow", "Progress Bar"))
        self.radioButton_start.setStatusTip(_translate("MainWindow", "Start the Progress Bar"))
        self.radioButton_start.setText(_translate("MainWindow", "Start"))
        self.radioButton_stop.setStatusTip(_translate("MainWindow", "Stop the Progress Bar"))
        self.radioButton_stop.setText(_translate("MainWindow", "Stop"))
        self.radioButton_reset.setStatusTip(_translate("MainWindow", "Reset the Progress Bar"))
        self.radioButton_reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Move the Dial"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_widgets_2), _translate("MainWindow", "Widgets 2"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Item 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Item 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Item 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Item 4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_drag_drop), _translate("MainWindow", "Drag && Drop"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_gl), _translate("MainWindow", "Open GL"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Client 1"))
        self.button_client_1.setText(_translate("MainWindow", "Connect to Server"))
        self.button_start_server.setText(_translate("MainWindow", "Start Server"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Client 2"))
        self.button_client_2.setText(_translate("MainWindow", "Connect to Server"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_network), _translate("MainWindow", "Network"))
        self.button_SQL_view_data.setText(_translate("MainWindow", "View Data"))
        self.button_SQL_add.setText(_translate("MainWindow", "Add Row"))
        self.button_SQL_delete.setText(_translate("MainWindow", "Delete Row"))
        self.button_SQL_create_db.setText(_translate("MainWindow", "Create DB"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_SQL), _translate("MainWindow", "SQL"))
        self.button_start_animation.setText(_translate("MainWindow", "Start animation"))
        self.button_stop_animation.setText(_translate("MainWindow", "Stop animation"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_animation), _translate("MainWindow", "Animation"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_CSS), _translate("MainWindow", "CSS"))
        self.statusbar.setStatusTip(_translate("MainWindow", "Status bar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())