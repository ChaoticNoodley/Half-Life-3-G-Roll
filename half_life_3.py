import os
import sys

# force locale
os.environ["LC_NUMERIC"] = "C"
import locale
try:
    locale.setlocale(locale.LC_NUMERIC, 'C')
except:
    pass

# otters imports
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QPixmap
import mpv

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Half-Life 3")
window.setWindowIcon(QIcon(resource_path("Half_Life_3icon.ico")))
window.setFixedSize(600, 800)

# Background
background = QLabel(window)
pixmap = QPixmap(resource_path("background.png"))
background.setPixmap(pixmap)
background.setScaledContents(True)
background.resize(600, 800)

text = QLabel("Compiling Shaders...\nPlease wait", window)
text.setStyleSheet("color: white; font-size: 18px;")
text.setAlignment(Qt.AlignmentFlag.AlignCenter)
text.setGeometry(0, 650, 600, 100)

# make windows video (QWidget)
video_container = QWidget(window)
video_container.setGeometry(0, 0, 1280, 720)
video_container.hide()

# MPV config
player = mpv.MPV(wid=str(int(video_container.winId())))


window.show()

def start_video():
    background.hide()
    text.hide()

    window.setFixedSize(1280, 720)
    screen = app.primaryScreen().size()
    window.move((screen.width() - 1280) // 2, (screen.height() - 720) // 2)

    video_container.show()
    
    video_path = resource_path("rickroll.webm")
    player.play(video_path)

# Fechar o app quando o vídeo acabar
@player.property_observer('eof-reached')
def on_end(name, value):
    if value:
        app.quit()

QTimer.singleShot(3000, start_video)

sys.exit(app.exec())
