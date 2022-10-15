from PySide6.QtWidgets import QApplication, QWidget
app = QApplication([])

#window = QWidget()
#window.show() 


window = QPushButton("Push Me")
window.show()

app.exec_()

print("Finished")