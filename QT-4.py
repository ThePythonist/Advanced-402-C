import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Window")
        self.setGeometry(500, 500, 700, 700)
        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the PyQt Window!")
        welcome_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(welcome_label)

        # layout.addStretch(1)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.on_submit_clicked)

        layout.addWidget(submit_button)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_submit_clicked(self):
        print("Submit button clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# In this example, we create a class `MainWindow` that inherits from `QMainWindow`.
# The initialization method `__init__()` sets the window title and geometry,
# and calls the `initUI()` method to create the user interface.
# The `initUI()` method creates the main widget, a vertical layout,
# and adds a welcome label and a submit button to the layout.
# The submit button's `clicked` signal is connected to the `on_submit_clicked()` method of the `MainWindow` class.
# The `on_submit_clicked()` method is a callback function that is called when the submit button is clicked.
# In this example, it simply prints a message to the console.
# Finally, we create an instance of `QApplication`, an instance of `MainWindow`,
# show the window, and start the application event loop.
