from brain import get_ai_response

messages = [
    {
        "role": "user",
        "content": "Chào Nahida!"
    },
    {
        "role": "user",
        "content": "Nahida ơi, hôm nay mình hơi mệt"
    }
]

reply = get_ai_response(messages)
print(reply)