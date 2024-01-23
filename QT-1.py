import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('My First Window')
window.resize(400, 400)

# to show the window
window.show()

# sys.exit ensure that the app exits when even loop ( app.exec ) is terminated
sys.exit(app.exec_())
