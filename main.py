import os
import sys
import models
from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Local AI prompt sender")
        self.setMinimumSize(800, 600)
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        layout.setContentsMargins(40, 40, 40, 40)

        self.model_selector = QComboBox()
        self.model_selector.addItem("Llama 3.3 70B")
        self.model_selector.addItem("Llama 3.1 8B")
        self.model_selector.addItem("Qwen3 32B")
        layout.addWidget(self.model_selector)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter your prompt: ")
        self.input_field.setFont(QFont("Arial", 20))
        self.input_field.returnPressed.connect(self.generate)
        layout.addWidget(self.input_field)

        self.send_btn = QPushButton("Send")
        self.send_btn.setFont(QFont("Arial", 20))
        self.send_btn.clicked.connect(self.generate)
        layout.addWidget(self.send_btn)

        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setFont(QFont("Arial", 20))
        layout.addWidget(self.output_field)

    def generate(self):
        choice = self.model_selector.currentIndex()
        user_input = self.input_field.text().strip()
        if not (user_input or choice):
            return
        self.output_field.setText("waiting the model response")
        self.send_btn.setEnabled(False)
        QApplication.processEvents()

        try:
            model = models.ModelFactory.get_model(choice)
            result = model.generate(user_input)
            self.output_field.setText(result)
        except Exception as e:
            self.output_field.setText(f"Hata: {str(e)}")
        finally:
            self.send_btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

