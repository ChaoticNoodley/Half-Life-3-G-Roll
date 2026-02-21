import sys, os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget


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

text = QLabel("Configuring sudo panda...\nPlease wait", window)
text.setStyleSheet("color: white; font-size: 18px;")
text.setAlignment(Qt.AlignmentFlag.AlignCenter)
text.setGeometry(0, 650, 600, 100)

video_widget = QVideoWidget(window)
video_widget.setGeometry(0, 0, 1280, 720)
video_widget.hide()

audio = QAudioOutput()
player = QMediaPlayer()
player.setAudioOutput(audio)

window.show()


def start_video():
    background.hide()
    text.hide()

    window.setFixedSize(1280, 720)
    screen = app.primaryScreen().size()
    window.move(
        (screen.width() - 1280) // 2,
        (screen.height() - 720) // 2
    )

    video_widget.setGeometry(0, 0, 1280, 720)
    video_widget.show()

    player.setVideoOutput(video_widget)

    video_path = resource_path("rickroll.mp4")
    player.setSource(QUrl.fromLocalFile(video_path))
    audio.setVolume(1.0)
    player.play()


def on_media_status(status):
    if status == QMediaPlayer.MediaStatus.EndOfMedia:
        app.quit()


player.mediaStatusChanged.connect(on_media_status)

QTimer.singleShot(3000, start_video)

sys.exit(app.exec())