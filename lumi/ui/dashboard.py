from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, 
                             QGridLayout, QPushButton, QProgressBar)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon, QColor

class DashboardWidget(QFrame):
    def __init__(self, title, value, icon=None, color="#00A8FF"):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(30, 30, 30, 200);
                border-radius: 15px;
                border: 1px solid {color}30;
            }}
        """)
        layout = QVBoxLayout(self)
        
        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("color: #888; font-size: 12px; font-weight: bold;")
        layout.addWidget(lbl_title)
        
        lbl_val = QLabel(value)
        lbl_val.setStyleSheet(f"color: {color}; font-size: 24px; font-weight: bold;")
        layout.addWidget(lbl_val)

class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # Grid of stats
        grid = QGridLayout()
        layout.addLayout(grid)
        
        # System Stats
        self.cpu_widget = DashboardWidget("CPU LOAD", "12%", color="#FF5555")
        self.mem_widget = DashboardWidget("MEMORY", "4.2 GB", color="#55FF55")
        self.net_widget = DashboardWidget("NETWORK", "ONLINE", color="#00A8FF")
        self.temp_widget = DashboardWidget("CORE TEMP", "45°C", color="#FFAA00")
        
        grid.addWidget(self.cpu_widget, 0, 0)
        grid.addWidget(self.mem_widget, 0, 1)
        grid.addWidget(self.net_widget, 1, 0)
        grid.addWidget(self.temp_widget, 1, 1)
        
        # Tasks / Active module
        self.task_frame = QFrame()
        self.task_frame.setStyleSheet("""
            background-color: rgba(20, 20, 20, 150);
            border-radius: 15px;
            padding: 10px;
        """)
        task_layout = QVBoxLayout(self.task_frame)
        task_layout.addWidget(QLabel("ACTIVE MODULES"))
        
        # Mock active modules
        for mod in ["Voice Recognition (Picovoice)", "Neural Cloud (ElevenLabs)", "Reasoning Core (Gemini/GPT)"]:
            lbl = QLabel(f"• {mod}")
            lbl.setStyleSheet("color: #CCC; font-family: Consolas; margin-left: 10px;")
            task_layout.addWidget(lbl)
            
        layout.addWidget(self.task_frame)
        
        # Add stretch to push everything up if needed
        # layout.addStretch()

    def update_weather(self, weather_str):
        # We could update a widget here
        pass
