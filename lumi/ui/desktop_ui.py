import sys
from PyQt6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, 
                             QLineEdit, QPushButton, QFrame, QHBoxLayout, 
                             QGraphicsDropShadowEffect, QStackedWidget)
from PyQt6.QtCore import Qt, QTimer, QPoint, QRect, pyqtSignal
from PyQt6.QtGui import QFont, QColor, QPalette, QBrush, QLinearGradient, QIcon
import qtawesome as qta

from lumi.ui.dashboard import DashboardUI

class LUMIUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LUMI AI")
        self.resize(1000, 700) # Wider for dashboard
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
        shadow.setColor(QColor(0, 168, 255, 100))
        self.central_widget.setGraphicsEffect(shadow)
        
        # Main Layout (HBox: Sidebar + Content)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # --- Sidebar ---
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(80)
        self.sidebar.setStyleSheet("""
            background-color: #1A1A1A;
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            border-right: 1px solid #333;
        """)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 30, 10, 30)
        self.sidebar_layout.setSpacing(20)
        
        # Nav Buttons
        self.btn_dashboard = self._create_nav_btn("fa5s.th-large", 0)
        self.btn_chat = self._create_nav_btn("fa5s.comments", 1)
        self.btn_browser = self._create_nav_btn("fa5b.chrome", 2) # Mock browser view
        
        self.sidebar_layout.addWidget(self.btn_dashboard)
        self.sidebar_layout.addWidget(self.btn_chat)
        self.sidebar_layout.addWidget(self.btn_browser)
        self.sidebar_layout.addStretch()
        
        # --- Content Area ---
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header (Close Button)
        self.header = QWidget()
        self.header.setFixedHeight(40)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(20, 10, 20, 0)
        
        title = QLabel("L U M I  //  OS")
        title.setStyleSheet("color: #666; font-family: Segoe UI; letter-spacing: 2px;")
        self.header_layout.addWidget(title)
        
        self.header_layout.addStretch()
        
        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.setStyleSheet("color: white; font-size: 20px; border: none; background: transparent;")
        self.close_btn.clicked.connect(self.close)
        self.header_layout.addWidget(self.close_btn)
        
        self.content_layout.addWidget(self.header)
        
        # Stacked Pages
        self.pages = QStackedWidget()
        self.content_layout.addWidget(self.pages)
        
        # Page 1: Dashboard
        self.dashboard_page = DashboardUI()
        self.pages.addWidget(self.dashboard_page)
        
        # Page 2: Chat (The old UI logic moved here)
        self.chat_page = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_page)
        
        # Orb
        self.status_label = QLabel("●")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Arial", 40))
        self.status_label.setStyleSheet("color: #00A8FF; margin: 10px;")
        self.chat_layout.addWidget(self.status_label)
        
        # Chat Box
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #000000;
                color: #B0B0B0;
                border-radius: 10px;
                padding: 10px;
                font-family: Consolas;
                font-size: 13px;
                border: 1px solid #333;
            }
        """)
        self.chat_layout.addWidget(self.chat_display)
        
        # Input
        input_container = QHBoxLayout()
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Execute Command...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #222;
                color: white;
                border: 1px solid #444;
                border-radius: 15px;
                padding: 10px;
            }
        """)
        input_container.addWidget(self.text_input)
        
        self.send_btn = QPushButton("➤")
        self.send_btn.setFixedSize(40, 40)
        self.send_btn.setStyleSheet("background-color: #00A8FF; color: white; border-radius: 20px;")
        input_container.addWidget(self.send_btn)
        self.chat_layout.addLayout(input_container)
        
        self.pages.addWidget(self.chat_page)
        
        # Page 3: Placeholder Browser
        browser_lbl = QLabel("SECURE BROWSER\n(INITIALIZING...)")
        browser_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        browser_lbl.setStyleSheet("color: #444; font-size: 20px;")
        self.pages.addWidget(browser_lbl)
        
        # Add to main
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.content_area)
        
        # Default Page
        self.pages.setCurrentIndex(1) # Start at Chat
        
        # Dragging logic
        self.old_pos = None

    def _create_nav_btn(self, icon_name, index):
        btn = QPushButton()
        btn.setIcon(qta.icon(icon_name, color="#666"))
        btn.setIconSize(QPoint(30, 30))
        btn.setFixedSize(60, 60)
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #333;
            }
        """)
        btn.clicked.connect(lambda: self.pages.setCurrentIndex(index))
        return btn

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
        html = f"<div style='color:{color}; text-align:{align}; margin-bottom:5px;'><b>{sender}:</b> {text}</div>"
        self.chat_display.append(html)
