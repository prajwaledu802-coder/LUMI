import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton, QFrame, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QTimer, QPoint, QRect
from PyQt6.QtGui import QFont, QColor, QPalette, QBrush, QLinearGradient

class LUMIUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LUMI AI")
        self.resize(500, 700)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Central Container
        self.central_widget = QFrame()
        self.central_widget.setStyleSheet("""
            QFrame {
                background-color: #0F0F0F;
                border-radius: 20px;
                border: 1px solid #333;
            }
        """)
        self.setCentralWidget(self.central_widget)
        
        # Dropshadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 168, 255, 100)) # Blue glow
        self.central_widget.setGraphicsEffect(shadow)
        
        # Layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        # Header (Close Button + Title)
        self.header = QWidget()
        self.header_layout = QHBoxLayout(self.header)
        self.header_title = QLabel("L U M I")
        self.header_title.setStyleSheet("color: #FFFFFF; font-weight: bold; font-family: Segoe UI;")
        self.header_layout.addWidget(self.header_title)
        
        self.header_layout.addStretch()
        
        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.setStyleSheet("color: white; font-size: 20px; border: none; background: transparent;")
        self.close_btn.clicked.connect(self.close)
        self.header_layout.addWidget(self.close_btn)
        
        self.layout.addWidget(self.header)
        
        # Status Orb (Animated via stylesheet updates)
        self.status_label = QLabel("●")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Arial", 40))
        self.status_label.setStyleSheet("color: #00A8FF; margin: 20px;")
        self.layout.addWidget(self.status_label)
        
        # Chat Display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #1A1A1A;
                color: #B0B0B0;
                border-radius: 10px;
                padding: 10px;
                font-family: Consolas;
                font-size: 13px;
                border: none;
            }
        """)
        self.layout.addWidget(self.chat_display)
        
        # Input Area
        self.input_area = QWidget()
        self.input_layout = QHBoxLayout(self.input_area)
        self.input_layout.setContentsMargins(0, 0, 0, 0)
        
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type a command...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #222;
                color: white;
                border: 1px solid #444;
                border-radius: 15px;
                padding: 10px;
                font-family: Segoe UI;
            }
            QLineEdit:focus {
                border: 1px solid #00A8FF;
            }
        """)
        self.input_layout.addWidget(self.text_input)
        
        self.send_btn = QPushButton("➤")
        self.send_btn.setFixedSize(40, 40)
        self.send_btn.setStyleSheet("""
            QPushButton {
                background-color: #00A8FF;
                color: white;
                border-radius: 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0088CC;
            }
        """)
        self.input_layout.addWidget(self.send_btn)
        
        self.layout.addWidget(self.input_area)

        # Dragging logic
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    def update_status(self, status):
        """Updates the status glowing orb."""
        if status == "LISTENING":
            self.status_label.setStyleSheet("color: #00FF00; font-size: 50px; text-shadow: 0 0 10px #00FF00;")
        elif status == "PROCESSING":
            self.status_label.setStyleSheet("color: #FFFF00; font-size: 50px; text-shadow: 0 0 10px #FFFF00;")
        elif status == "RESPONDING":
            self.status_label.setStyleSheet("color: #00A8FF; font-size: 50px; text-shadow: 0 0 20px #00A8FF;")
        else:
            self.status_label.setStyleSheet("color: #333333; font-size: 40px;")
    
    def add_message(self, sender, text):
        color = "#00A8FF" if sender == "LUMI" else "#FFFFFF"
        align = "left" if sender == "LUMI" else "right"
        # Simple HTML formatting
        html = f"<div style='color:{color}; text-align:{align}; margin-bottom:5px;'><b>{sender}:</b> {text}</div>"
        self.chat_display.append(html)
