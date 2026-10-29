from brain import get_ai_response
from memory import load_messages, save_message, search_messages

def main():
    print("Nahida: Chào cậu! Hôm nay mình cùng học gì nào? 🌱")

    conversation_history = [
    {"role": role, "content": content}
    for role, content in load_messages()
    ]

    print("Loaded messages:", len(conversation_history))

    while True:
        message = input("You: ")

        if message.lower() == 'exit':
            print("Nahida: Tạm biệt nhé!")
            break

        if message.strip() == "":
            print("Nahida: Cậu chưa nói gì mà!")
            continue

        if message.startswith("/search "):
            keyword = message[8:].strip()
            result = search_messages(keyword)


            if not result:
                print("Nahida không tìm thấy kí ức nào")
            else:
                for role, content in result:
                    print(f"{role}: {content}")

            continue

        conversation_history.append({
                                            "role" : "user",
                                            "content" : message
                                        })

        save_message("user", message)

        recent_history = conversation_history[-10:]

        reply = get_ai_response(recent_history)
        print(f"Nahida: {reply}")

        conversation_history.append({
                                    "role" : "assistant",
                                    "content" : reply
                                })

        save_message("assistant", reply)



if __name__ == "__main__":
    main()
