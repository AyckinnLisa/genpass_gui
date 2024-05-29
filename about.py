# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(300, 440)
        about_window.setMinimumSize(QtCore.QSize(300, 440))
        about_window.setMaximumSize(QtCore.QSize(300, 440))
        about_window.setWindowTitle("")
        about_window.setStyleSheet("QWidget {    background-color: #5A5A5A; }\n"
"\n"
"QPushButton {\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #3a3a3a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed { background-color: #2d5bd4; }")
        self.close_btn = QtWidgets.QPushButton(parent=about_window)
        self.close_btn.setGeometry(QtCore.QRect(190, 360, 101, 32))
        self.close_btn.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close_btn.setFont(font)
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.title_desc_lbl = QtWidgets.QLabel(parent=about_window)
        self.title_desc_lbl.setGeometry(QtCore.QRect(0, 55, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_desc_lbl.setFont(font)
        self.title_desc_lbl.setStyleSheet("background-color: rgb(22, 97, 167);")
        self.title_desc_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.title_desc_lbl.setObjectName("title_desc_lbl")
        self.title_lbl = QtWidgets.QLabel(parent=about_window)
        self.title_lbl.setGeometry(QtCore.QRect(0, 0, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(48)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("background-color: rgb(22, 97, 167);")
        self.title_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setIndent(-1)
        self.title_lbl.setObjectName("title_lbl")
        self.ver_lbl = QtWidgets.QLabel(parent=about_window)
        self.ver_lbl.setGeometry(QtCore.QRect(15, 115, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ver_lbl.setFont(font)
        self.ver_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.ver_lbl.setObjectName("ver_lbl")
        self.version_lbl = QtWidgets.QLabel(parent=about_window)
        self.version_lbl.setGeometry(QtCore.QRect(85, 115, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.version_lbl.setFont(font)
        self.version_lbl.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.version_lbl.setObjectName("version_lbl")
        self.site_link_lbl = QtWidgets.QLabel(parent=about_window)
        self.site_link_lbl.setGeometry(QtCore.QRect(85, 250, 145, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.site_link_lbl.setFont(font)
        self.site_link_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.site_link_lbl.setText("")
        self.site_link_lbl.setObjectName("site_link_lbl")
        self.about_mail_lbl = QtWidgets.QLabel(parent=about_window)
        self.about_mail_lbl.setGeometry(QtCore.QRect(85, 270, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.about_mail_lbl.setFont(font)
        self.about_mail_lbl.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.about_mail_lbl.setText("")
        self.about_mail_lbl.setObjectName("about_mail_lbl")
        self.label_3 = QtWidgets.QLabel(parent=about_window)
        self.label_3.setGeometry(QtCore.QRect(0, 410, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=about_window)
        self.label_5.setGeometry(QtCore.QRect(5, 105, 289, 97))
        self.label_5.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius: 5px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.info_lbl = QtWidgets.QLabel(parent=about_window)
        self.info_lbl.setGeometry(QtCore.QRect(20, 85, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_lbl.setFont(font)
        self.info_lbl.setObjectName("info_lbl")
        self.written_lbl = QtWidgets.QLabel(parent=about_window)
        self.written_lbl.setGeometry(QtCore.QRect(15, 155, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.written_lbl.setFont(font)
        self.written_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.written_lbl.setText("")
        self.written_lbl.setObjectName("written_lbl")
        self.language_lbl = QtWidgets.QLabel(parent=about_window)
        self.language_lbl.setGeometry(QtCore.QRect(85, 155, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.language_lbl.setFont(font)
        self.language_lbl.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.language_lbl.setText("")
        self.language_lbl.setObjectName("language_lbl")
        self.codeby_lbl = QtWidgets.QLabel(parent=about_window)
        self.codeby_lbl.setGeometry(QtCore.QRect(15, 175, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.codeby_lbl.setFont(font)
        self.codeby_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.codeby_lbl.setText("")
        self.codeby_lbl.setObjectName("codeby_lbl")
        self.author_lbl = QtWidgets.QLabel(parent=about_window)
        self.author_lbl.setGeometry(QtCore.QRect(85, 175, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.author_lbl.setFont(font)
        self.author_lbl.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.author_lbl.setObjectName("author_lbl")
        self.label_14 = QtWidgets.QLabel(parent=about_window)
        self.label_14.setGeometry(QtCore.QRect(80, 290, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=about_window)
        self.label_15.setGeometry(QtCore.QRect(10, 250, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.label_15.setObjectName("label_15")
        self.link_lbl = QtWidgets.QLabel(parent=about_window)
        self.link_lbl.setGeometry(QtCore.QRect(20, 218, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.link_lbl.setFont(font)
        self.link_lbl.setText("")
        self.link_lbl.setObjectName("link_lbl")
        self.label_17 = QtWidgets.QLabel(parent=about_window)
        self.label_17.setGeometry(QtCore.QRect(80, 250, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=about_window)
        self.label_18.setGeometry(QtCore.QRect(10, 290, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=about_window)
        self.label_19.setGeometry(QtCore.QRect(80, 270, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=about_window)
        self.label_20.setGeometry(QtCore.QRect(10, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=about_window)
        self.label_21.setGeometry(QtCore.QRect(5, 240, 289, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius: 5px;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.st_lbl = QtWidgets.QLabel(parent=about_window)
        self.st_lbl.setGeometry(QtCore.QRect(15, 250, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.st_lbl.setFont(font)
        self.st_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.st_lbl.setObjectName("st_lbl")
        self.label_23 = QtWidgets.QLabel(parent=about_window)
        self.label_23.setGeometry(QtCore.QRect(15, 270, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.label_23.setObjectName("label_23")
        self.git_lbl = QtWidgets.QLabel(parent=about_window)
        self.git_lbl.setGeometry(QtCore.QRect(15, 290, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.git_lbl.setFont(font)
        self.git_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.git_lbl.setObjectName("git_lbl")
        self.github_lbl = QtWidgets.QLabel(parent=about_window)
        self.github_lbl.setGeometry(QtCore.QRect(85, 290, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.github_lbl.setFont(font)
        self.github_lbl.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.github_lbl.setText("")
        self.github_lbl.setObjectName("github_lbl")
        self.release_lbl = QtWidgets.QLabel(parent=about_window)
        self.release_lbl.setGeometry(QtCore.QRect(15, 135, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.release_lbl.setFont(font)
        self.release_lbl.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.release_lbl.setText("")
        self.release_lbl.setObjectName("release_lbl")
        self.date_lbl = QtWidgets.QLabel(parent=about_window)
        self.date_lbl.setGeometry(QtCore.QRect(85, 135, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_lbl.setFont(font)
        self.date_lbl.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.date_lbl.setText("")
        self.date_lbl.setObjectName("date_lbl")
        self.changelog_btn = QtWidgets.QPushButton(parent=about_window)
        self.changelog_btn.setGeometry(QtCore.QRect(80, 360, 101, 32))
        self.changelog_btn.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.changelog_btn.setFont(font)
        self.changelog_btn.setText("")
        self.changelog_btn.setObjectName("changelog_btn")
        self.label_5.raise_()
        self.title_lbl.raise_()
        self.close_btn.raise_()
        self.title_desc_lbl.raise_()
        self.ver_lbl.raise_()
        self.version_lbl.raise_()
        self.label_3.raise_()
        self.info_lbl.raise_()
        self.written_lbl.raise_()
        self.language_lbl.raise_()
        self.codeby_lbl.raise_()
        self.author_lbl.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.link_lbl.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.site_link_lbl.raise_()
        self.st_lbl.raise_()
        self.label_23.raise_()
        self.about_mail_lbl.raise_()
        self.git_lbl.raise_()
        self.github_lbl.raise_()
        self.release_lbl.raise_()
        self.date_lbl.raise_()
        self.changelog_btn.raise_()

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        self.title_desc_lbl.setText(_translate("about_window", "Ayckinn\'s Password Generator"))
        self.title_lbl.setText(_translate("about_window", "GENPASS"))
        self.ver_lbl.setText(_translate("about_window", "Version : "))
        self.version_lbl.setText(_translate("about_window", "1.0"))
        self.label_3.setText(_translate("about_window", "Copyright ©2024 - Brooklyn softwares"))
        self.info_lbl.setText(_translate("about_window", "Informations"))
        self.author_lbl.setText(_translate("about_window", "Ayckinn"))
        self.label_14.setText(_translate("about_window", "Ayckinn"))
        self.label_15.setText(_translate("about_window", "Version : "))
        self.label_17.setText(_translate("about_window", "1.0"))
        self.label_18.setText(_translate("about_window", "Coded by :"))
        self.label_19.setText(_translate("about_window", "Python"))
        self.label_20.setText(_translate("about_window", "Written in :"))
        self.st_lbl.setText(_translate("about_window", "Site :"))
        self.label_23.setText(_translate("about_window", "Mail :"))
        self.git_lbl.setText(_translate("about_window", "Github : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QWidget()
    ui = Ui_about_window()
    ui.setupUi(about_window)
    about_window.show()
    sys.exit(app.exec())
