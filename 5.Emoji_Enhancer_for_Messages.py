emoji = {
    "love": "❤️",
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "surprised": "😲",
    "code": "💻",
    "coffee": "☕",
    "star": "⭐",
    "fire": "🔥",
    "music": "🎵",
    "food": "🍔",
    "travel": "✈️"
}

user_msg = input("Enter your message: ")
for word in user_msg.split():
    cleaned_word = word.lower().strip(".,!?")
    e = emoji.get(cleaned_word, "")
    if e:
        user_msg = user_msg.replace(word, f"{word}{e} ")

print("Enhanced Message: \n", user_msg)