import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('My First Window')
window.resize(500,500)

css1 = """
background-color:white;
"""
window.setStyleSheet(css1)

# Create a welcome label at the top center
label_1 = QLabel('Welcome', parent=window)
label_1.setGeometry(0, 50, window.width(), 50)
label_1.setAlignment(Qt.AlignCenter)

# to show the window
window.show()

# sys.exit ensure that the app exits when even loop ( app.exec ) is terminated
sys.exit(app.exec_())
