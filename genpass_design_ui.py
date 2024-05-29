# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genpass_design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_GenPass(object):
    def setupUi(self, GenPass):
        if not GenPass.objectName():
            GenPass.setObjectName(u"GenPass")
        GenPass.resize(488, 440)
        GenPass.setMinimumSize(QSize(488, 440))
        GenPass.setMaximumSize(QSize(488, 440))
        self.actionAbout = QAction(GenPass)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionChangelog = QAction(GenPass)
        self.actionChangelog.setObjectName(u"actionChangelog")
        self.actionQuit_GenPass = QAction(GenPass)
        self.actionQuit_GenPass.setObjectName(u"actionQuit_GenPass")
        self.actionQuit_GenPass.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
        self.actionQuit_GenPass.setShortcutVisibleInContextMenu(True)
        self.GenPass_Widget = QWidget(GenPass)
        self.GenPass_Widget.setObjectName(u"GenPass_Widget")
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(13)
        self.GenPass_Widget.setFont(font)
        self.GenPass_Widget.setStyleSheet(u"QWidget {	background-color: #1e1e1e; }\n"
"\n"
"QPushButton {\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	padding: 5px;\n"
"	background-color: #3a3a3a;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed { background-color: #2d5bd4; }")
        self.pass_len_lbl = QLabel(self.GenPass_Widget)
        self.pass_len_lbl.setObjectName(u"pass_len_lbl")
        self.pass_len_lbl.setGeometry(QRect(10, 140, 161, 20))
        self.select_char_lbl = QLabel(self.GenPass_Widget)
        self.select_char_lbl.setObjectName(u"select_char_lbl")
        self.select_char_lbl.setGeometry(QRect(10, 92, 221, 16))
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(13)
        self.select_char_lbl.setFont(font1)
        self.note_pass_lbl = QLabel(self.GenPass_Widget)
        self.note_pass_lbl.setObjectName(u"note_pass_lbl")
        self.note_pass_lbl.setGeometry(QRect(0, 310, 491, 20))
        self.note_pass_lbl.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.note_pass_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.generate_btn = QPushButton(self.GenPass_Widget)
        self.generate_btn.setObjectName(u"generate_btn")
        self.generate_btn.setGeometry(QRect(122, 195, 241, 32))
        self.generate_btn.setCheckable(True)
        self.password_lbl = QLabel(self.GenPass_Widget)
        self.password_lbl.setObjectName(u"password_lbl")
        self.password_lbl.setGeometry(QRect(10, 260, 71, 16))
        self.created_pass_entry = QLineEdit(self.GenPass_Widget)
        self.created_pass_entry.setObjectName(u"created_pass_entry")
        self.created_pass_entry.setGeometry(QRect(83, 253, 291, 32))
        self.created_pass_entry.setMaxLength(32)
        self.created_pass_entry.setCursorPosition(0)
        self.created_pass_entry.setReadOnly(True)
        self.length_spinbox = QSpinBox(self.GenPass_Widget)
        self.length_spinbox.setObjectName(u"length_spinbox")
        self.length_spinbox.setGeometry(QRect(177, 135, 41, 32))
        self.length_spinbox.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.length_spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.length_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.length_spinbox.setMinimum(3)
        self.length_spinbox.setMaximum(32)
        self.length_spinbox.setValue(8)
        self.layoutWidget = QWidget(self.GenPass_Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 390, 191, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.about_btn = QPushButton(self.layoutWidget)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(0, 32))

        self.horizontalLayout.addWidget(self.about_btn)

        self.close_btn = QPushButton(self.layoutWidget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 32))

        self.horizontalLayout.addWidget(self.close_btn)

        self.title_lbl = QLabel(self.GenPass_Widget)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setGeometry(QRect(0, 0, 488, 61))
        font2 = QFont()
        font2.setFamilies([u"Impact"])
        font2.setPointSize(48)
        self.title_lbl.setFont(font2)
        self.title_lbl.setStyleSheet(u"background-color: rgb(22, 97, 167);")
        self.title_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setIndent(-1)
        self.title_desc_lbl = QLabel(self.GenPass_Widget)
        self.title_desc_lbl.setObjectName(u"title_desc_lbl")
        self.title_desc_lbl.setGeometry(QRect(0, 52, 488, 20))
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(11)
        self.title_desc_lbl.setFont(font3)
        self.title_desc_lbl.setStyleSheet(u"background-color: rgb(22, 97, 167);")
        self.title_desc_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.minmax_lbl = QLabel(self.GenPass_Widget)
        self.minmax_lbl.setObjectName(u"minmax_lbl")
        self.minmax_lbl.setGeometry(QRect(250, 140, 181, 20))
        self.copy_btn = QPushButton(self.GenPass_Widget)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setGeometry(QRect(383, 253, 88, 32))
        self.program_closed_lbl = QLabel(self.GenPass_Widget)
        self.program_closed_lbl.setObjectName(u"program_closed_lbl")
        self.program_closed_lbl.setGeometry(QRect(0, 330, 491, 20))
        self.program_closed_lbl.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.program_closed_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.no_retrieve_lbl = QLabel(self.GenPass_Widget)
        self.no_retrieve_lbl.setObjectName(u"no_retrieve_lbl")
        self.no_retrieve_lbl.setGeometry(QRect(0, 350, 491, 20))
        self.no_retrieve_lbl.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.no_retrieve_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget1 = QWidget(self.GenPass_Widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(240, 90, 222, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lower_chkbx = QCheckBox(self.layoutWidget1)
        self.lower_chkbx.setObjectName(u"lower_chkbx")
        self.lower_chkbx.setFont(font1)
        self.lower_chkbx.setChecked(True)

        self.horizontalLayout_2.addWidget(self.lower_chkbx)

        self.upper_chkbx = QCheckBox(self.layoutWidget1)
        self.upper_chkbx.setObjectName(u"upper_chkbx")
        self.upper_chkbx.setFont(font)
        self.upper_chkbx.setChecked(True)

        self.horizontalLayout_2.addWidget(self.upper_chkbx)

        self.digits_chkbx = QCheckBox(self.layoutWidget1)
        self.digits_chkbx.setObjectName(u"digits_chkbx")
        self.digits_chkbx.setFont(font)
        self.digits_chkbx.setChecked(True)

        self.horizontalLayout_2.addWidget(self.digits_chkbx)

        self.symbols_chkbx = QCheckBox(self.layoutWidget1)
        self.symbols_chkbx.setObjectName(u"symbols_chkbx")
        self.symbols_chkbx.setFont(font)
        self.symbols_chkbx.setChecked(False)

        self.horizontalLayout_2.addWidget(self.symbols_chkbx)

        GenPass.setCentralWidget(self.GenPass_Widget)

        self.retranslateUi(GenPass)

        QMetaObject.connectSlotsByName(GenPass)
    # setupUi

    def retranslateUi(self, GenPass):
        GenPass.setWindowTitle(QCoreApplication.translate("GenPass", u"GenPass v1.0", None))
        self.actionAbout.setText(QCoreApplication.translate("GenPass", u"About", None))
#if QT_CONFIG(statustip)
        self.actionAbout.setStatusTip(QCoreApplication.translate("GenPass", u"About GenPass", None))
#endif // QT_CONFIG(statustip)
        self.actionChangelog.setText(QCoreApplication.translate("GenPass", u"Changelog", None))
#if QT_CONFIG(statustip)
        self.actionChangelog.setStatusTip(QCoreApplication.translate("GenPass", u"Changelog", None))
#endif // QT_CONFIG(statustip)
        self.actionQuit_GenPass.setText(QCoreApplication.translate("GenPass", u"Quit GenPass", None))
#if QT_CONFIG(statustip)
        self.actionQuit_GenPass.setStatusTip(QCoreApplication.translate("GenPass", u"Close the program", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionQuit_GenPass.setShortcut(QCoreApplication.translate("GenPass", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.pass_len_lbl.setText(QCoreApplication.translate("GenPass", u"Select password's length :", None))
        self.select_char_lbl.setText(QCoreApplication.translate("GenPass", u"Select your password's characters :", None))
        self.note_pass_lbl.setText("")
        self.generate_btn.setText(QCoreApplication.translate("GenPass", u" Generate password", None))
        self.password_lbl.setText(QCoreApplication.translate("GenPass", u"Password :", None))
        self.created_pass_entry.setText("")
        self.about_btn.setText(QCoreApplication.translate("GenPass", u" About ", None))
        self.close_btn.setText(QCoreApplication.translate("GenPass", u" Close", None))
        self.title_lbl.setText(QCoreApplication.translate("GenPass", u"GENPASS", None))
        self.title_desc_lbl.setText(QCoreApplication.translate("GenPass", u"Ayckinn's Password Generator", None))
        self.minmax_lbl.setText(QCoreApplication.translate("GenPass", u"Minimum : 3 / Maximum : 32", None))
        self.copy_btn.setText(QCoreApplication.translate("GenPass", u" Copy", None))
        self.program_closed_lbl.setText("")
        self.no_retrieve_lbl.setText("")
        self.lower_chkbx.setText(QCoreApplication.translate("GenPass", u" a-z", None))
        self.upper_chkbx.setText(QCoreApplication.translate("GenPass", u" A-Z", None))
        self.digits_chkbx.setText(QCoreApplication.translate("GenPass", u" 0-9", None))
        self.symbols_chkbx.setText(QCoreApplication.translate("GenPass", u" $%@", None))
    # retranslateUi

