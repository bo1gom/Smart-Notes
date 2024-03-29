# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 623)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field_text = QtWidgets.QTextEdit(self.centralwidget)
        self.field_text.setGeometry(QtCore.QRect(10, 10, 261, 561))
        self.field_text.setObjectName("field_text")
        self.button_note_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_note_save.setGeometry(QtCore.QRect(290, 230, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_note_save.setFont(font)
        self.button_note_save.setObjectName("button_note_save")
        self.button_note_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_note_del.setGeometry(QtCore.QRect(470, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_note_del.setFont(font)
        self.button_note_del.setObjectName("button_note_del")
        self.list_notes = QtWidgets.QListWidget(self.centralwidget)
        self.list_notes.setGeometry(QtCore.QRect(290, 20, 371, 181))
        self.list_notes.setObjectName("list_notes")
        self.button_note_create = QtWidgets.QPushButton(self.centralwidget)
        self.button_note_create.setGeometry(QtCore.QRect(290, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_note_create.setFont(font)
        self.button_note_create.setObjectName("button_note_create")
        self.button_teg_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_teg_add.setGeometry(QtCore.QRect(290, 500, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_teg_add.setFont(font)
        self.button_teg_add.setObjectName("button_teg_add")
        self.button_teg_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_teg_search.setGeometry(QtCore.QRect(290, 530, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_teg_search.setFont(font)
        self.button_teg_search.setObjectName("button_teg_search")
        self.button_teg_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_teg_del.setGeometry(QtCore.QRect(480, 500, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_teg_del.setFont(font)
        self.button_teg_del.setObjectName("button_teg_del")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 671, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.list_tags_ladel = QtWidgets.QLabel(self.centralwidget)
        self.list_tags_ladel.setGeometry(QtCore.QRect(290, 280, 661, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_tags_ladel.setFont(font)
        self.list_tags_ladel.setObjectName("list_tags_ladel")
        self.field_tag = QtWidgets.QLineEdit(self.centralwidget)
        self.field_tag.setGeometry(QtCore.QRect(290, 480, 371, 20))
        self.field_tag.setObjectName("field_tag")
        self.list_tags = QtWidgets.QListWidget(self.centralwidget)
        self.list_tags.setGeometry(QtCore.QRect(295, 301, 361, 181))
        self.list_tags.setObjectName("list_tags")
        self.field_text.raise_()
        self.button_note_save.raise_()
        self.button_note_del.raise_()
        self.list_notes.raise_()
        self.button_note_create.raise_()
        self.button_teg_add.raise_()
        self.button_teg_search.raise_()
        self.button_teg_del.raise_()
        self.list_tags_ladel.raise_()
        self.field_tag.raise_()
        self.label.raise_()
        self.list_tags.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_note_save.setText(_translate("MainWindow", "зробити замітку"))
        self.button_note_del.setText(_translate("MainWindow", "видалити замітку "))
        self.button_note_create.setText(_translate("MainWindow", "створити замітку"))
        self.button_teg_add.setText(_translate("MainWindow", "додани замітки "))
        self.button_teg_search.setText(_translate("MainWindow", "шукати замітки по тегу"))
        self.button_teg_del.setText(_translate("MainWindow", "відкріпити від замітки"))
        self.label.setText(_translate("MainWindow", "список заміток"))
        self.list_tags_ladel.setText(_translate("MainWindow", "список тегів "))
        self.field_tag.setText(_translate("MainWindow", "Введіть тег..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
