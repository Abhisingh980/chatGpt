from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
import backend


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("chatbot")

        self.setMinimumSize(600, 500)

        # add chat Window
        self.chat_window = QTextEdit(self)
        self.chat_window.setGeometry(10, 10, 400, 300)
        self.chat_window.setReadOnly(True)

        # add input text
        self.input_text = QLineEdit(self)
        self.input_text.setGeometry(10, 320, 400, 40)

        # add button
        self.search = QPushButton("Search", self)
        self.search.setGeometry(420, 320, 80, 40)
        self.search.clicked.connect(self.set_text)

    def set_text(self):
        call_class = backend.ChatBot()
        response = call_class.get_response(self.input_text)
        self.chat_window.setText(response)





app = QApplication(sys.argv)
chat_bot = ChatWindow()
chat_bot.show()
sys.exit(app.exec())


