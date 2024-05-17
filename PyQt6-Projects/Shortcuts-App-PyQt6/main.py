import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Open Notion Work Example")
        self.setGeometry(100, 100, 300, 150)

        # Create a button for opening Notion Work
        self.notion_work_button = QPushButton("Notion Work", self)
        self.notion_work_button.move(50, 50)
        self.notion_work_button.clicked.connect(self.open_notion_work)

    def open_notion_work(self):
        url = "https://www.notion.so/gerozayas/WORK-Classes-f0cd3a126a434731ab0c08a32ae44d6d"
        command = ["firefox", "--new-window", url]
        try:
            subprocess.run(command, check=True)
            print("Opened Notion Work successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to open Notion Work: {e}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
