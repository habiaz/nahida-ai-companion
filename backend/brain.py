import requests

def get_ai_response(recent_history):
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
                        "Do not pretend to be a human."
                        "When a user asks for their own name, Nahida must rely on the conversation history to provide the answer,"
                        " ensuring she does not mistake it for her own name."
                        "When speaking Vietnamese, always use mình "
                        "avoid using tôi, bạn, quý khách")
            },
        ] + recent_history,
        "stream" : False
    }

    response = requests.post("http://localhost:11434/api/chat", json=payload)

    data = response.json()

    return data["message"]["content"]

if __name__ == "__main__":
    print(get_ai_response([
        {
            "role" : "user",
            "content" : "Hello Nahida!"
        }
    ]))