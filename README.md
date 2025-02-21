# Voice-Enabled AI Assistant

This project is a voice-enabled AI assistant that integrates **speech-to-text (STT)**, **AI processing**, and **text-to-speech (TTS)** capabilities. It allows users to interact with an AI model (powered by Ollama) using voice commands. The assistant listens to the user's speech, processes the input using the Ollama API, and responds back in spoken form.

---

## Introduction

The goal of this project is to create a seamless voice-based interaction system with an AI model. It leverages the **Vosk** library for speech-to-text conversion, the **Ollama API** for AI-based query processing, and **pyttsx3** for text-to-speech functionality. This assistant can be used for tasks like answering questions, providing information, or engaging in conversational interactions.

---

## Technology Stack

- **Vosk**: A lightweight and efficient speech recognition library used for converting spoken words into text.
- **Ollama**: An AI API that processes the transcribed text and generates intelligent responses using the `llama2:latest` model.
- **Pyttsx3**: A text-to-speech library that converts the AI's response into spoken audio.

---

## Pipeline

1. **Speech-to-Text (STT)**:
   - The user speaks into the microphone.
   - The Vosk library captures the audio and transcribes it into text.

2. **AI Processing**:
   - The transcribed text is sent to the Ollama API.
   - The AI model processes the input and generates a response.

3. **Text-to-Speech (TTS)**:
   - The AI's response is converted into speech using pyttsx3.
   - The assistant speaks the response back to the user.

4. **Loop**:
   - The process repeats, allowing for continuous interaction.

---

## How to Use the Code

### Prerequisites

1. Ensure Python 3.x is installed on your system.
2. Clone the Repository:
    ```bash
    git clone https://github.com/your-repo/voice-enabled-ai-assistant.git
    cd voice-enabled-ai-assistant
    ```
3. Install the required Python libraries using the following command:
   ```bash
   pip install requests pyaudio pyttsx3 vosk
   ```
4. Download the Vosk model and place it in the `models` directory. You can download the model from [here](https://alphacephei.com/vosk/models).
5. Ensure that the Ollama API must be running locally at `http://localhost:11434`.
6. Run the Script:
    ```bash
    python main.py
    ```
7. Interact with the Assistant by speaking into your microphone when prompted. The assistant will process your speech, generate a response, and speak it back to you.

---

## Limitations
- The accuracy of speech-to-text conversion depends on the quality of the speech-to-text(STT) model and the clarity of the user's speech. 
- The AI's responses are limited by the capabilities of the Ollama model being used to process requests (i.e., quantized small models might be less accurate than large models).
- The text-to-speech functionality may not sound perfectly natural.

## Future Enhancements
- Add support for multiple languages in speech recognition and text-to-speech.
- Integrate with cloud-based AI models for improved response quality.
- Add a graphical user interface (GUI) for better user interaction.
- Implement context-aware conversations for more natural interactions.

