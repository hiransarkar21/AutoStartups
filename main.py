# imports
from PyQt5.QtWidgets import *
from interfaces import main_window
import sys


# main function
def main():
    if __name__ == "__main__":
        application = QApplication(sys.argv)
        window = main_window.MainWindow()
        window.show()
        application.exec()


main()
