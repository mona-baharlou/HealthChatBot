
from textblob import TextBlob
import requests
import json


def detect_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def generate_response(user_input, mood):
    prompt = f"""
You are a kind and supportive mental health assistant.
The user said: "{user_input}"
Their mood appears to be: {mood}.
Please respond with a short and empathetic message to comfort and support the user.
"""
    #base url for local ollama
    url = "http://localhost:11434/api/chat"


    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()

        # Read streaming response safely
        full_response = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "message" in data and "content" in data["message"]:
                    full_response += data["message"]["content"]

        return full_response.strip()

    except Exception as e:
        return f" Error contacting local model: {e}"

if __name__ == "__main__":
    print(" Welcome to your local mental health assistant.")
    user_input = input("How are you feeling today?\n>> ")
    mood = detect_mood(user_input)
    print(f"\n Detected mood: {mood}")

    reply = generate_response(user_input, mood)
    print("\n Chatbot:\n" + reply)

   