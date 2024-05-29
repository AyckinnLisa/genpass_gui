# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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

class Ui_about_window(object):
    def setupUi(self, about_window):
        if not about_window.objectName():
            about_window.setObjectName(u"about_window")
        about_window.resize(300, 450)
        about_window.setMinimumSize(QSize(300, 450))
        about_window.setMaximumSize(QSize(300, 450))
        about_window.setStyleSheet(u"QWidget {	background-color: #1e1e1e; }\n"
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
        self.close_btn = QPushButton(about_window)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(200, 360, 87, 32))
        self.close_btn.setMinimumSize(QSize(0, 32))
        self.title_desc_lbl = QLabel(about_window)
        self.title_desc_lbl.setObjectName(u"title_desc_lbl")
        self.title_desc_lbl.setGeometry(QRect(0, 52, 301, 20))
        font = QFont()
        font.setPointSize(11)
        self.title_desc_lbl.setFont(font)
        self.title_desc_lbl.setStyleSheet(u"background-color: rgb(22, 97, 167);")
        self.title_desc_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.title_lbl = QLabel(about_window)
        self.title_lbl.setObjectName(u"title_lbl")
        self.title_lbl.setGeometry(QRect(0, 0, 301, 61))
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(48)
        self.title_lbl.setFont(font1)
        self.title_lbl.setStyleSheet(u"background-color: rgb(22, 97, 167);")
        self.title_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setIndent(-1)
        self.label = QLabel(about_window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 51, 16))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(11)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(about_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 110, 21, 16))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.site_link_lbl = QLabel(about_window)
        self.site_link_lbl.setObjectName(u"site_link_lbl")
        self.site_link_lbl.setGeometry(QRect(80, 240, 145, 16))
        self.site_link_lbl.setFont(font3)
        self.site_link_lbl.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.site_link_lbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.about_mail_lbl = QLabel(about_window)
        self.about_mail_lbl.setObjectName(u"about_mail_lbl")
        self.about_mail_lbl.setGeometry(QRect(80, 260, 141, 16))
        self.about_mail_lbl.setFont(font3)
        self.about_mail_lbl.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.about_mail_lbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(about_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 410, 301, 41))
        self.label_3.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(about_window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(5, 100, 289, 101))
        self.label_5.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-radius: 5px;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5.setMargin(2)
        self.label_9 = QLabel(about_window)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 78, 100, 20))
        font4 = QFont()
        font4.setPointSize(10)
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_10 = QLabel(about_window)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 150, 71, 16))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_11 = QLabel(about_window)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 150, 211, 16))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_12 = QLabel(about_window)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 170, 71, 16))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_13 = QLabel(about_window)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(80, 170, 51, 16))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_14 = QLabel(about_window)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(80, 280, 51, 16))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_15 = QLabel(about_window)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 240, 51, 16))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_16 = QLabel(about_window)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 208, 100, 20))
        self.label_16.setFont(font4)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_17 = QLabel(about_window)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(80, 240, 21, 16))
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_18 = QLabel(about_window)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 280, 71, 16))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_19 = QLabel(about_window)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(80, 260, 51, 16))
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_20 = QLabel(about_window)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 260, 71, 16))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_21 = QLabel(about_window)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(5, 230, 289, 81))
        self.label_21.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-radius: 5px;")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_21.setMargin(2)
        self.label_22 = QLabel(about_window)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 240, 41, 16))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_23 = QLabel(about_window)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 260, 41, 16))
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_24 = QLabel(about_window)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 280, 51, 16))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.github_lbl = QLabel(about_window)
        self.github_lbl.setObjectName(u"github_lbl")
        self.github_lbl.setGeometry(QRect(80, 280, 141, 16))
        self.github_lbl.setFont(font3)
        self.github_lbl.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.github_lbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_4 = QLabel(about_window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 61, 16))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_6 = QLabel(about_window)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 130, 111, 16))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 235);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.changelog_btn = QPushButton(about_window)
        self.changelog_btn.setObjectName(u"changelog_btn")
        self.changelog_btn.setGeometry(QRect(86, 360, 101, 32))
        self.changelog_btn.setMinimumSize(QSize(0, 32))
        self.label_5.raise_()
        self.title_lbl.raise_()
        self.close_btn.raise_()
        self.title_desc_lbl.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.site_link_lbl.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.about_mail_lbl.raise_()
        self.label_24.raise_()
        self.github_lbl.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.changelog_btn.raise_()

        self.retranslateUi(about_window)

        QMetaObject.connectSlotsByName(about_window)
    # setupUi

    def retranslateUi(self, about_window):
        about_window.setWindowTitle(QCoreApplication.translate("about_window", u"About GenPass", None))
        self.close_btn.setText(QCoreApplication.translate("about_window", u" Close", None))
        self.title_desc_lbl.setText(QCoreApplication.translate("about_window", u"Ayckinn's Password Generator", None))
        self.title_lbl.setText(QCoreApplication.translate("about_window", u"GENPASS", None))
        self.label.setText(QCoreApplication.translate("about_window", u"Version : ", None))
        self.label_2.setText(QCoreApplication.translate("about_window", u"1.0", None))
        self.site_link_lbl.setText("")
        self.about_mail_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("about_window", u"Copyright \u00a92024 - Brooklyn softwares", None))
        self.label_5.setText("")
        self.label_9.setText(QCoreApplication.translate("about_window", u"Informations", None))
        self.label_10.setText(QCoreApplication.translate("about_window", u"Written in :", None))
        self.label_11.setText(QCoreApplication.translate("about_window", u"Python and PyQt6", None))
        self.label_12.setText(QCoreApplication.translate("about_window", u"Coded by :", None))
        self.label_13.setText(QCoreApplication.translate("about_window", u"Ayckinn", None))
        self.label_14.setText(QCoreApplication.translate("about_window", u"Ayckinn", None))
        self.label_15.setText(QCoreApplication.translate("about_window", u"Version : ", None))
        self.label_16.setText(QCoreApplication.translate("about_window", u"Links", None))
        self.label_17.setText(QCoreApplication.translate("about_window", u"1.0", None))
        self.label_18.setText(QCoreApplication.translate("about_window", u"Coded by :", None))
        self.label_19.setText(QCoreApplication.translate("about_window", u"Python", None))
        self.label_20.setText(QCoreApplication.translate("about_window", u"Written in :", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("about_window", u"Site :", None))
        self.label_23.setText(QCoreApplication.translate("about_window", u"Mail :", None))
        self.label_24.setText(QCoreApplication.translate("about_window", u"Github : ", None))
        self.github_lbl.setText("")
        self.label_4.setText(QCoreApplication.translate("about_window", u"Released :", None))
        self.label_6.setText(QCoreApplication.translate("about_window", u"May 20' 2024", None))
        self.changelog_btn.setText(QCoreApplication.translate("about_window", u" Changelog", None))
    # retranslateUi

