# imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from string import Template
import sys
import os
import requests

# BASE DIRECTORIES
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# master class
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # global attributes
        self.screen_size = QApplication.primaryScreen().availableSize()

        self.heading_font = QFont("Poppins",  self.screen_size.height() // 60)
        self.heading_font.setWordSpacing(1.5)
        self.heading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.subheading_font = QFont("Montserrat", self.screen_size.height() // 75)
        self.subheading_font.setWordSpacing(1.5)
        self.subheading_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.paragraph_font = QFont("Montserrat", self.screen_size.height() // 88)
        self.paragraph_font.setWordSpacing(1.5)
        self.paragraph_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.context_menu_font = QFont("Montserrat",  self.screen_size.height() // 96)
        self.context_menu_font.setWordSpacing(1.5)
        self.context_menu_font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

        self.oldPos = self.pos()

        # instance methods
        self.window_configurations()
        self.master_user_interface()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.active_auto_startups_container:
            # context menu
            context_menu = QMenu()

            # actions of the context menu
            disable_record = QAction("Disable Record")
            disable_record.setFont(self.context_menu_font)
            disable_record.setIcon(QIcon("assets/disable_icon.png"))

            enable_record = QAction("Enable Record")
            enable_record.setFont(self.context_menu_font)
            enable_record.setIcon(QIcon("assets/enable_icon.png"))
            
            delete_record = QAction("Delete Record")
            delete_record.setFont(self.context_menu_font)
            delete_record.setIcon(QIcon("assets/delete_icon.png"))

            hide_item = QAction("Hide Record")
            hide_item.setFont(self.context_menu_font)
            hide_item.setIcon(QIcon("assets/hide_icon.png"))

            # adding actions to the context menu
            context_menu.addAction(disable_record)
            context_menu.addAction(enable_record)
            context_menu.addAction(delete_record)
            context_menu.addAction(hide_item)

            menu_click = context_menu.exec(event.globalPos())

            # picking out the item on which the context menu is activated
            try:
                item = source.itemAt(event.pos())
            except Exception as error:
                # I know I should have left the clause broad, I shall update it sometime soon
                pass

            # check the option clicked and run the respective if/elif/else block
            if menu_click == disable_record:
                pass
            elif menu_click == enable_record:
                pass
            elif menu_click == delete_record:
                pass
            elif menu_click == hide_item:
                pass
            else:
                pass

            return True
        return super(MainWindow, self).eventFilter(source, event)

    def center(self):
        # center the mainwindow
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        # track mouse press events inside the window
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # track mouse move event inside the window
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def window_configurations(self):
        # holds all the configurations related to the MainWindow
        self.setFixedSize(int(self.screen_size.width() // 2.2), int(self.screen_size.height() // 1.3))
        self.setWindowFlag(Qt.FramelessWindowHint)

    def master_user_interface(self):
        # holds all the widgets and layouts of the current window
        self.master_layout = QVBoxLayout()
        self.toolbar_layout  = QHBoxLayout()
        self.header_layout = QHBoxLayout()
        self.body_layout = QVBoxLayout()
        self.footer_layout = QHBoxLayout()

        # toolbar icons with functionalities
        self.close_window = QPushButton()
        self.close_window.setIcon(QIcon("assets/close_icon.png"))
        self.close_window.setIconSize(QSize(20, 20))
        self.close_window.clicked.connect(self.close_window_clicked)
        self.close_window.setStyleSheet("""QPushButton{border: 0px;}""")

        # application name
        application_name = QLabel()
        application_name.setText("AutoStartups")
        application_name.setFont(self.heading_font)

        # settings button
        settings_button = QPushButton()
        settings_button.setText("  Configurations")
        settings_button.setFont(self.subheading_font)
        settings_button.setIcon(QIcon("assets/settings_icon.png"))
        settings_button.setIconSize(QSize(self.screen_size.width() // 96, self.screen_size.height() // 54))
        settings_button.setFixedSize(self.screen_size.width() // 8, self.screen_size.height() // 18)
        settings_button.setStyleSheet(str(Template("""QPushButton{border: 2px solid black;  border-radius: ${radius}px;}""").substitute(radius=self.screen_size.height() // 36)))

        # active auto-startups label
        active_auto_startups_label = QLabel()
        active_auto_startups_label.setFont(self.subheading_font)
        active_auto_startups_label.setText("Active Auto Startups Programs and Files")

        self.active_auto_startups_container = QListWidget()
        self.active_auto_startups_container.installEventFilter(self)
        self.active_auto_startups_container.setFont(self.paragraph_font)
        self.active_auto_startups_container.addItem("PyCram Community Edition")

        # adding widgets to child layouts
        self.toolbar_layout.setContentsMargins(5, 5, 5, 5)
        self.toolbar_layout.addWidget(self.close_window, alignment=Qt.AlignRight)

        self.header_layout.setContentsMargins(40, 20, 40, 20)
        self.header_layout.addWidget(application_name)
        self.header_layout.addWidget(settings_button)

        self.body_layout.setContentsMargins(40, 20, 40, 20)
        self.body_layout.addWidget(active_auto_startups_label)
        self.body_layout.addWidget(self.active_auto_startups_container)

        # adding child layouts to master layout
        self.master_layout.addLayout(self.toolbar_layout)
        self.master_layout.addLayout(self.header_layout)
        self.master_layout.addLayout(self.body_layout)
        self.master_layout.addLayout(self.footer_layout)

        self.setLayout(self.master_layout)

    def close_window_clicked(self):
        self.close()
