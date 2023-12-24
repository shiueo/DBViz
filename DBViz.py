import html
import os
import sys
import webbrowser

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QScrollArea, QTextEdit, \
    QSizePolicy

from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))


def openReportIssueLink():
    webbrowser.open("https://github.com/Schtarn/DBViz/issues")


def openCommunityLink():
    webbrowser.open("https://discord.gg/NXwVfdcygM")


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About DBViz")
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))
        self.setMinimumSize(640, 360)

        layout = QVBoxLayout()

        # Scrollable area for license text
        license_scroll_area = QScrollArea(self)
        license_text = QTextEdit(self)
        license_text.setReadOnly(True)  # Make it read-only
        license_text.setHtml(self.about_text())  # Load license text
        license_scroll_area.setWidget(license_text)

        # Set properties for the QScrollArea
        license_scroll_area.setWidgetResizable(True)
        license_scroll_area.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        layout.addWidget(license_scroll_area)

        with open(
                file=global_path.get_proj_abs_path("themes/standard_dark.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        self.setLayout(layout)
        self.setWindowTitle("About DBViz")

    def about_text(self):
        text = "<html><head><style>h1 { color: #FF0A54; font-size: 18px; }</style></head><body>"
        text+= "<h1>VERSION</h1>"

        text += "<h1>LICENSE</h1>"
        with open(global_path.get_proj_abs_path("LICENSE")) as f:
            license_content = f.read()
            escaped_license_content = html.escape(license_content)
            text += f"<pre>{escaped_license_content}</pre>"

        version_info = "Version 0.0.1"  # Replace this with your actual version information
        text += f"<h1>{version_info}</h1>"

        text += "</body></html>"
        return text


class DBViz_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)

        # menuBar_File -------------------------------------------------------------------------------
        fileMenu = menuBar.addMenu("&File")

        fileMenu_NewWorkSpaceAction = QAction(
            "New Workspace",
            self,
        )
        fileMenu_ExitAction = QAction(
            "Exit",
            self,
        )
        fileMenu_ExitAction.triggered.connect(DBViz_QApplication.quit)

        fileMenu.addAction(fileMenu_NewWorkSpaceAction)
        fileMenu.addSeparator()
        fileMenu.addAction(fileMenu_ExitAction)
        # menuBar_File -------------------------------------------------------------------------------

        editMenu = menuBar.addMenu("&Edit")

        # menuBar_Help -------------------------------------------------------------------------------
        helpMenu = menuBar.addMenu("&Help")

        helpMenu_ReportIssueAction = QAction(
            "Report Issue...",
            self,
        )
        helpMenu_ReportIssueAction.triggered.connect(openReportIssueLink)

        helpMenu_CommunityAction = QAction(
            "Community (Schtarn Discord)",
            self,
        )
        helpMenu_CommunityAction.triggered.connect(openCommunityLink)

        helpMenu_AboutAction = QAction(
            "About DBViz",
            self,
        )
        helpMenu_AboutAction.triggered.connect(self.openAboutDialog)

        helpMenu.addAction(helpMenu_ReportIssueAction)
        helpMenu.addAction(helpMenu_CommunityAction)
        helpMenu.addSeparator()
        helpMenu.addAction(helpMenu_AboutAction)
        # menuBar_Help -------------------------------------------------------------------------------

        self.setWindowTitle("DBViz")
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))
        self.setMinimumSize(640, 360)
        self.resize(1280, 720)
        self.initUI()

    def initUI(self):
        with open(
                file=global_path.get_proj_abs_path("themes/standard_dark.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

    def openAboutDialog(self):
        about_dialog = AboutDialog()
        about_dialog.exec()


if __name__ == "__main__":
    DBViz_QApplication = QApplication()
    DBViz_GUI = DBViz_MainWindow()
    DBViz_GUI.show()
    sys.exit(DBViz_QApplication.exec())
