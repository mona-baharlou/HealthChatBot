# Local Mental Health Chatbot (Offline, LLM + Sentiment Detection)

This project is a simple, fully **offline mental health chatbot** that detects your mood using **sentiment analysis (TextBlob)** and responds with an empathetic message generated by a **local LLM (LLaMA 3.2)**. No internet connection or API keys are needed.

Great for privacy-conscious users, mental health projects, or learning how to combine LLMs with NLP tools.


## Features

- Text-based CLI chatbot
- Mood detection via `TextBlob` (positive / neutral / negative)
- Local response generation using `llama3.2` 
- 100% offline — no API key
- Simple, portable Python script

---

## Requirements

- **Ollama** installed from [https://ollama.com](https://ollama.com)
- Model pulled locally (e.g. `llama3.2`)

# Example Interaction

Welcome to your local mental health assistant.
How are you feeling today?
> I'm feeling stressed and alone.

Detected mood: negative

Chatbot:
I'm really sorry you're feeling that way. You're not alone, and it's okay to take a step back. You're doing your best, and that matters. 

# How It Works
 - Takes user input from terminal.
 - Uses TextBlob to analyze the sentiment.
 - Constructs a prompt describing the mood.
 - Sends it to a local LLM (via Ollama HTTP API).
 - Streams and prints the chatbot's empathetic response.

# Future Improvements
  Log conversation history
