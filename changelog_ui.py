# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changelog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_changelog(object):
    def setupUi(self, changelog):
        if not changelog.objectName():
            changelog.setObjectName(u"changelog")
        changelog.resize(341, 235)
        changelog.setMinimumSize(QSize(341, 235))
        changelog.setMaximumSize(QSize(341, 235))
        changelog.setStyleSheet(u"QWidget {	background-color: #1e1e1e; }\n"
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
        self.changelog_close_btn = QPushButton(changelog)
        self.changelog_close_btn.setObjectName(u"changelog_close_btn")
        self.changelog_close_btn.setGeometry(QRect(260, 190, 71, 32))
        self.changelog_close_btn.setMinimumSize(QSize(0, 32))
        self.title_desc_lbl = QLabel(changelog)
        self.title_desc_lbl.setObjectName(u"title_desc_lbl")
        self.title_desc_lbl.setGeometry(QRect(0, 50, 341, 20))
        font = QFont()
        font.setPointSize(11)
        self.title_desc_lbl.setFont(font)
        self.title_desc_lbl.setStyleSheet(u"background-color: rgb(22, 97, 167);")
        self.title_desc_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.title_lbl = QLabel(changelog)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setGeometry(QRect(0, -2, 341, 61))
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(48)
        self.title_lbl.setFont(font1)
        self.title_lbl.setStyleSheet(u"background-color: rgb(22, 97, 167);")
        self.title_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setIndent(-1)
        self.label_9 = QLabel(changelog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 75, 100, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_4 = QLabel(changelog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 101, 16))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(11)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_5 = QLabel(changelog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 321, 61))
        self.label_5.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-radius: 5px;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5.setMargin(2)
        self.label_6 = QLabel(changelog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 130, 311, 16))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.title_lbl.raise_()
        self.label_5.raise_()
        self.changelog_close_btn.raise_()
        self.title_desc_lbl.raise_()
        self.label_9.raise_()
        self.label_4.raise_()
        self.label_6.raise_()

        self.retranslateUi(changelog)

        QMetaObject.connectSlotsByName(changelog)
    # setupUi

    def retranslateUi(self, changelog):
        changelog.setWindowTitle(QCoreApplication.translate("changelog", u"Changelog", None))
        self.changelog_close_btn.setText(QCoreApplication.translate("changelog", u" Close", None))
        self.title_desc_lbl.setText(QCoreApplication.translate("changelog", u"Ayckinn's Password Generator", None))
        self.title_lbl.setText(QCoreApplication.translate("changelog", u"GENPASS", None))
        self.label_9.setText(QCoreApplication.translate("changelog", u"Version 1.0", None))
        self.label_4.setText(QCoreApplication.translate("changelog", u"- Initial release", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("changelog", u"- Add \"copy\" button to save the password", None))
    # retranslateUi

