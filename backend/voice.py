import edge_tts
import asyncio
import pygame

VOICE = "en-US-JennyNeural"
VOICE_VI = "vi-VN-HoaiMyNeural"

def detect_voice(text):
    vietnamese_chars = "ăâđêôơưàáảãạèéẻẽẹìíỉĩịòóỏõọùúủũụỳýỷỹỵ"

    if any(char in text.lower() for char in vietnamese_chars):
        return VOICE_VI

    return VOICE

async def speak(text, voice = None):
    if voice is None:
        voice = detect_voice(text)
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("nahida_voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("nahida_voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(speak("Hello! I'm Nahida!"))