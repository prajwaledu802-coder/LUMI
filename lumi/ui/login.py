from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QFrame, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, pyqtSignal, QPropertyAnimation, QEasingCurve, QPoint
from PyQt6.QtGui import QColor, QFont, QLinearGradient, QBrush, QPalette

class LoginUI(QWidget):
    login_successful = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 700)
        self.setStyleSheet("background-color: transparent;")
        
        # Central Card
        self.card = QFrame(self)
        self.card.setGeometry(50, 100, 400, 500)
        self.card.setStyleSheet("""
            QFrame {
                background-color: rgba(20, 20, 20, 240);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        
        # Glow Effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 168, 255, 60))
        self.card.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(self.card)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title using LUMI font style
        title = QLabel("L U M I")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #00A8FF; font-size: 48px; font-weight: bold; letter-spacing: 5px; font-family: Segoe UI;")
        layout.addWidget(title)
        
        subtitle = QLabel("ACCESS TERMINAL")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #666; font-size: 12px; letter-spacing: 2px; margin-bottom: 30px;")
        layout.addWidget(subtitle)
        
        # Inputs
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("IDENTITY")
        self.user_input.setStyleSheet(self._input_style())
        layout.addWidget(self.user_input)
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("PASSKEY")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_input.setStyleSheet(self._input_style())
        layout.addWidget(self.pass_input)
        
        # Spacer
        layout.addSpacing(20)
        
        # Login Button
        self.login_btn = QPushButton("INITIALIZE")
        self.login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #00A8FF;
                color: white;
                border-radius: 25px;
                height: 50px;
                font-weight: bold;
                font-size: 14px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background-color: #0088CC;
                border: 2px solid #00A8FF;
            }
        """)
        self.login_btn.clicked.connect(self.authenticate)
        layout.addWidget(self.login_btn)
        
        # Footer
        footer = QLabel("SECURE CONNECTION ESTABLISHED")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet("color: #444; font-size: 10px; margin-top: 20px;")
        layout.addWidget(footer)

    def _input_style(self):
        return """
            QLineEdit {
                background-color: rgba(255, 255, 255, 10);
                color: white;
                border: 1px solid rgba(255, 255, 255, 30);
                border-radius: 10px;
                padding: 15px;
                font-size: 13px;
                font-family: Consolas;
                margin-bottom: 10px;
            }
            QLineEdit:focus {
                border: 1px solid #00A8FF;
                background-color: rgba(0, 168, 255, 10);
            }
        """

    def authenticate(self):
        # Professional mock auth
        user = self.user_input.text()
        pwd = self.pass_input.text()
        
        if user and pwd: # Accept anything for prototype
            self.animate_success()
        else:
            self.user_input.setPlaceholderText("REQUIRED")

    def animate_success(self):
        self.login_btn.setText("ACCESS GRANTED")
        self.login_btn.setStyleSheet("background-color: #00FF00; color: black; border-radius: 25px; height: 50px; font-weight: bold;")
        # Simple timer to trigger signal
        QPropertyAnimation(self, b"windowOpacity").start() # Placeholder
        self.login_successful.emit()
