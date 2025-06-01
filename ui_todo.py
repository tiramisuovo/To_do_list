# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'To_do_list_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-image: url(:/pink_lavender_background.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: none;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"/* Fix line edits and combo boxes too */\n"
"QLineEdit, QComboBox {\n"
"    background: none;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"")
        self.Add = QPushButton(self.centralwidget)
        self.Add.setObjectName(u"Add")
        self.Add.setGeometry(QRect(440, 30, 91, 21))
        self.Add.setStyleSheet(u"")
        self.Delete = QPushButton(self.centralwidget)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setGeometry(QRect(660, 60, 91, 23))
        self.List = QTreeWidget(self.centralwidget)
        self.List.setObjectName(u"List")
        self.List.setGeometry(QRect(30, 130, 741, 371))
        self.List.setColumnCount(4)
        self.Title_input = QLineEdit(self.centralwidget)
        self.Title_input.setObjectName(u"Title_input")
        self.Title_input.setGeometry(QRect(360, 80, 113, 20))
        self.Task_title = QLabel(self.centralwidget)
        self.Task_title.setObjectName(u"Task_title")
        self.Task_title.setGeometry(QRect(390, 60, 51, 16))
        self.Task_title.setAlignment(Qt.AlignCenter)
        self.Task_desc = QLabel(self.centralwidget)
        self.Task_desc.setObjectName(u"Task_desc")
        self.Task_desc.setGeometry(QRect(500, 60, 91, 16))
        self.Task_desc.setAlignment(Qt.AlignCenter)
        self.Desc_input = QLineEdit(self.centralwidget)
        self.Desc_input.setObjectName(u"Desc_input")
        self.Desc_input.setGeometry(QRect(490, 80, 113, 20))
        self.Mytodolist = QLabel(self.centralwidget)
        self.Mytodolist.setObjectName(u"Mytodolist")
        self.Mytodolist.setGeometry(QRect(30, 40, 281, 51))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        self.Mytodolist.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"Add New Task", None))
        self.Delete.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))
        ___qtreewidgetitem = self.List.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Priority", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Mark as done", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Task", None));
        self.Task_title.setText(QCoreApplication.translate("MainWindow", u"Task Title", None))
        self.Task_desc.setText(QCoreApplication.translate("MainWindow", u"Task Description", None))
        self.Mytodolist.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#625160;\">My To-do List </span><span style=\" font-size:22pt; font-weight:600; color:#ffffce;\">\u2728</span></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

