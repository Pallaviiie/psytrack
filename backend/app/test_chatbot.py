from app.chatbot.chatbot_engine import chatbot_reply

while True:

    print("\n" + "=" * 60)

    message = input("You : ")

    if message.lower() == "exit":
        break

    response = chatbot_reply(message)

    print("\nPrediction :", response["prediction"])
    print("Confidence :", response["confidence"])
    print("Emergency  :", response["emergency"])
    print("Bot :", response["reply"])