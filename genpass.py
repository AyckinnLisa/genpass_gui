
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
from genpass_design import Ui_GenPass
import buttons, about, changelog, lang, lang_mode

import os
os.system('clear')
# -- To get the icons path
basedir = os.path.dirname(__file__)

from pathlib import Path
user_home_path = str(Path.home())


class GenPass(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(GenPass, self).__init__(*args, **kwargs)

        self.gui = Ui_GenPass()
        self.gui.setupUi(self)

    '''
    =======================================================
    ==               LANG WINDOW MANAGEMENT              ==
    =======================================================
    '''
    def show_lang_window(self) -> None:
        self.lang_window = QMainWindow()
        self.langwin = lang.Ui_Lang()
        self.langwin.setupUi(self.lang_window)

        self.lang_window.show()
        self.hide()

        '''
            If the function is not called with LAMBDA, App returns a TypeError : NoneType
            Close the -LANG_WINDOWS- at FIRST and run the app function
        '''
        # -- English button --
        self.langwin.en_btn.clicked.connect(lambda: self.lang_window.close())
        self.langwin.en_btn.clicked.connect(lambda: self.save_lang_file('en'))
        self.langwin.en_btn.clicked.connect(lambda: self.run_app(lang_mode.en_lbl, lang_mode.en_btn))

        # -- French button --
        self.langwin.fr_btn.clicked.connect(lambda: self.lang_window.close())
        self.langwin.fr_btn.clicked.connect(lambda: self.save_lang_file('fr'))
        self.langwin.fr_btn.clicked.connect(lambda: self.run_app(lang_mode.fr_lbl, lang_mode.fr_btn))


    def save_lang_file(self, lang):
        with open(user_home_path + '/.genpassconfig', 'w') as slf:
            slf.write(lang)


    def run_app(self, lbl, btn) -> None:
        self.show()
        
        #-- Main labels --
        self.gui.select_char_lbl.setText(lbl[0])
        self.gui.pass_len_lbl.setText(lbl[1])
        self.gui.password_lbl.setText(lbl[2])

        # -- Generate button --
        self.gui.generate_btn.setIcon(QIcon(os.path.join(basedir, "icons", "generate.png")))
        self.gui.generate_btn.clicked.connect(lambda: self.generate_new_password(lbl))
        self.gui.generate_btn.setText(btn[0])

        #-- Copy button --
        self.gui.copy_btn.setIcon(QIcon(os.path.join(basedir, "icons", "copy.png")))
        self.gui.copy_btn.clicked.connect(lambda: self.copy_password(lbl))
        self.gui.copy_btn.setText(btn[1])

        # -- About button --
        self.gui.about_btn.setIcon(QIcon(os.path.join(basedir, "icons", "about.png")))
        self.gui.about_btn.clicked.connect(lambda: self.show_about_window(lbl, btn))
        self.gui.about_btn.setText(btn[2])

        # -- Exit button --
        self.gui.close_btn.setIcon(QIcon(os.path.join(basedir, "icons", "close.png")))
        self.gui.close_btn.clicked.connect(app.quit)
        self.gui.close_btn.setText(btn[3])

    # -------------------------------------------------------------------------
    '''
        This function shuffles the characters 
        and create a new password with the characters and length choosen by the user
    '''
    def generate_length_of_pass(self, length: int, characters: str) -> str:
        from secrets import choice

        return ''.join(choice(characters) for _ in range(length))

    # -------------------------------------------------------------------------
    '''
        This function retrieves each characters combination contained in the buttons.py module
        If the checkbox is checked, it adds each value one after the other
    '''
    def get_chars(self) -> str:
        chars = ""

        for chkbox in buttons.Characters:
            if getattr(self.gui, chkbox.name).isChecked():
                chars += chkbox.value

        return chars
    
    # -------------------------------------------------------------------------
    '''
        This function clears the length input focus,
        displays the generated password with length and character values
        and displays a warning message to avoid forgetting to save the password
    '''
    def generate_new_password(self, lbl) -> None:
        self.gui.created_pass_entry.setFocus()

        self.gui.created_pass_entry.setText(
            self.generate_length_of_pass(
                length=self.gui.length_spinbox.value(),
                characters=self.get_chars()))
        
        self.gui.note_pass_lbl.setText(lbl[3])
            
    # -------------------------------------------------------------------------
    def copy_password(self, lbl) -> None:
        if self.gui.created_pass_entry.text() == "":
            self.gui.note_pass_lbl.setText(lbl[7])
        else:
            QApplication.clipboard().setText(self.gui.created_pass_entry.text())

            self.gui.note_pass_lbl.setText(lbl[6])

    '''
    =======================================================
    ==               ABOUT WINDOW MANAGENT               ==
    =======================================================
    '''
    def show_about_window(self, lbl, btn) -> None:
        self.aboutw = QMainWindow()
        self.abwin = about.Ui_about_window()
        self.abwin.setupUi(self.aboutw)
        self.aboutw.setWindowTitle(lbl[8])

        self.aboutw.show()
        self.hide()

        # == Informations ==
        self.abwin.release_lbl.setText(lbl[9])
        self.abwin.date_lbl.setText(lbl[10])
        self.abwin.written_lbl.setText(lbl[11])
        self.abwin.language_lbl.setText(lbl[12])
        self.abwin.codeby_lbl.setText(lbl[13])

        # == Links ==
        self.abwin.link_lbl.setText(lbl[14])
        # -- Site --
        self.abwin.site_link_lbl.setText('<a href=https://www.ayckinn.fr>www.ayckinn.fr</a>')
        self.abwin.site_link_lbl.setOpenExternalLinks(True)
        # -- Contact --
        self.abwin.about_mail_lbl.setText('<a href=mailto:contact@ayckinn.fr>contact@ayckinn.fr</a>')
        self.abwin.about_mail_lbl.setOpenExternalLinks(True)
        # -- Github --
        self.abwin.github_lbl.setText('<a href=https://github.com/AyckinnLisa?tab=repositories>Repositories</a>')
        self.abwin.github_lbl.setOpenExternalLinks(True)

        # -- Close button --
        self.abwin.close_btn.setIcon(QIcon(os.path.join(basedir, "icons", "close.png")))
        self.abwin.close_btn.clicked.connect(self.close_about_window)
        self.abwin.close_btn.setText(btn[4])
        # -- Changelog button --
        self.abwin.changelog_btn.setIcon(QIcon(os.path.join(basedir, "icons", "changelog.png")))
        self.abwin.changelog_btn.clicked.connect(lambda: self.show_changelog_window(lbl, btn))
        self.abwin.changelog_btn.setText(btn[5])

    # The button closes the "About" window et displays the main window with function below
    def close_about_window(self) -> None:
        self.aboutw.close()
        self.show()

    '''
    =======================================================
    ==            CHANGELOG WINDOW MANAGEMENT            ==
    =======================================================
    '''
    def show_changelog_window(self, lbl, btn) -> None:
        self.changelog_window = QMainWindow()
        self.changewin = changelog.Ui_changelog()
        self.changewin.setupUi(self.changelog_window)
        self.changelog_window.setWindowTitle(lbl[15])

        self.changelog_window.show()
        self.aboutw.hide()

        self.changewin.chlog_close_btn.setIcon(QIcon(os.path.join(basedir, "icons", "close.png")))
        self.changewin.chlog_close_btn.clicked.connect(self.close_changelog_window)
        self.changewin.chlog_close_btn.setText(btn[4])

        self.changewin.chlog_line_1_lbl.setText(lbl[16])
        self.changewin.chlog_line_2_lbl.setText(lbl[17])
        self.changewin.chlog_line_3_lbl.setText(lbl[18])
        

    def close_changelog_window(self) -> None:
        self.changelog_window.close()
        self.show()



import sys

app = QApplication(sys.argv)
# -- Add App icon here --
app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "icon.png")))

widget = GenPass()

if os.path.exists(user_home_path + '/.genpassconfig'):
    with open(user_home_path + '/.genpassconfig') as sf:
        for line in sf:
            if line == "fr":
                widget.run_app(lang_mode.fr_lbl, lang_mode.fr_btn)
            elif line == "en":
                widget.run_app(lang_mode.en_lbl, lang_mode.en_btn)
    widget.show()
else:
    widget.show_lang_window()

app.exec()
