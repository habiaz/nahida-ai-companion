from brain import get_ai_response

def main():
    print("Nahida: Chào cậu! Hôm nay mình cùng học gì nào? 🌱")

    while True:
        message = input("You: ")

        if message.lower() == 'exit':
            print("Nahida: Tạm biệt nhé!")
            break

        if message.strip() == "":
            print("Nahida: Cậu chưa nói gì mà!")
            continue

        reply = get_ai_response(message)
        print(f"Nahida: {reply}")


if __name__ == "__main__":
    main()
