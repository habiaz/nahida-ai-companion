import requests

def get_ai_response(message):
    payload = {
        "model" : "qwen2.5:3b",
        "messages" : [
            {
                "role" : "system",
                "content" : (
                        "You are Nahida, a friendly AI study companion. "
                        "Your primary purpose is to help users practice IELTS, "
                        "learn programming, and have natural conversations. "
                        "Speak warmly and naturally. Keep your answers concise. "
                        "Introduce yourself as Nahida when asked your name. "
                        "Do not pretend to be a human.")
            },
            {
                "role" : "user",
                "content" : message
            },
        ],
        "stream" : False
    }

    response = requests.post("http://localhost:11434/api/chat", json=payload)

    data = response.json()

    return data["message"]["content"]

if __name__ == "__main__":
    print(get_ai_response("Hello Nahida!"))