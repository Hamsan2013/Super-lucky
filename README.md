# Super Lucky — Hamsan's Pi Buddy

Super Lucky is a personal assistant app for Raspberry Pi that uses OpenAI for the full "Lucky" personality, provides voice + chat, and can control the Pi (apps, shell commands, GPIO).

**Features**
- Chat window + TTS voice replies (pyttsx3)
- Voice recording + optional offline speech-to-text using VOSK
- OpenAI integration for full Lucky personality (uses `OPENAI_API_KEY` in env)
- Command execution with confirmation prompts
- Desktop launcher and icon (place `logo.png` in repo)

**Important:** Do NOT commit your OpenAI key to GitHub. Set it on the Pi only:
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
source ~/.bashrc
