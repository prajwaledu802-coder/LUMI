from PyQt6.QtWidgets import QSplashScreen, QProgressBar, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QPixmap, QFont, QColor, QPainter, QLinearGradient

class CinematicSplash(QSplashScreen):
    def __init__(self):
        # Create a faux-screen map to draw on
        pixmap = QPixmap(600, 350)
        pixmap.fill(QColor("#050505")) # Deep black/grey
        super().__init__(pixmap)
        
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        
        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Logo / Title
        self.title = QLabel("L U M I")
        self.title.setFont(QFont("Segoe UI", 48, QFont.Weight.Bold))
        self.title.setStyleSheet("color: #00A8FF; letter-spacing: 10px;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)
        
        # Subtitle
        self.subtitle = QLabel("INTELLIGENCE ARCHITECTURE INITIALIZING...")
        self.subtitle.setFont(QFont("Consolas", 10))
        self.subtitle.setStyleSheet("color: #555555;")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.subtitle)
        
        # Progress Bar
        self.progress = QProgressBar()
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #00A8FF;
                border-radius: 5px;
                text-align: center;
                background-color: #111;
                color: white;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0055aa, stop:1 #00A8FF);
                width: 20px;
            }
        """)
        self.progress.setFixedWidth(400)
        self.progress.setFixedHeight(10)
        self.layout.addWidget(self.progress)
        
        self.progress_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30) # Fast updates

    def update_progress(self):
        self.progress_value += 1
        self.progress.setValue(self.progress_value)
        
        if self.progress_value > 100:
            self.timer.stop()
            self.close()

    def drawContents(self, painter):
        # We are using widgets instead of raw painting for easier layout
        pass
