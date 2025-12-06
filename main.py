import sys
import threading
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QMessageBox
)

from lucky_ai import LuckyAI
from voice import record_audio, TTS
from actions import run_command, is_dangerous

class LuckyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Super Lucky")
        self.setMinimumSize(700, 500)

        self.ai = LuckyAI()
        self.tts = TTS()

        layout = QVBoxLayout()

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        layout.addWidget(self.chat)

        h = QHBoxLayout()
        self.input = QLineEdit()
        self.input.returnPressed.connect(self.on_send)
        h.addWidget(self.input)

        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.on_send)
        h.addWidget(send_btn)

        layout.addLayout(h)

        voice_btn = QPushButton("🎤 Voice (5 sec)")
        voice_btn.clicked.connect(self.on_voice)
        layout.addWidget(voice_btn)

        self.setLayout(layout)

    def append(self, text):
        self.chat.append(text)

    def confirm(self, msg):
        r = QMessageBox.question(self, "Confirm", msg,
                                 QMessageBox.Yes | QMessageBox.No)
        return r == QMessageBox.Yes

    def on_send(self):
        msg = self.input.text().strip()
        if not msg:
            return
        self.append(f"You: {msg}")
        self.input.clear()
        threading.Thread(target=self.process, args=(msg,), daemon=True).start()

    def process(self, msg):
        # Shell command
        if msg.startswith("run "):
            cmd = msg[4:]

            if is_dangerous(cmd):
                if not self.confirm(f"Dangerous command:\n{cmd}\nAre you sure?"):
                    self.append("Lucky: Command cancelled.")
                    return

            if not self.confirm(f"Run command?\n{cmd}"):
                self.append("Lucky: Cancelled.")
                return

            out = run_command(cmd)
            self.append(f"Lucky (shell):\n{out}")
            return

        # AI response
        reply = self.ai.chat(msg)
        self.append(f"Lucky: {reply}")
        self.tts.speak(reply)

    def on_voice(self):
        try:
            self.append("Recording...")
            fp = record_audio(5)
            self.append("Recorded audio saved.")
            self.append("Lucky: Voice transcription not added yet, type message instead.")
        except Exception as e:
            self.append(f"Voice error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LuckyApp()
    w.show()
    sys.exit(app.exec())
