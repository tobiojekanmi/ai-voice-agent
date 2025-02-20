import os
import json
import requests
import pyaudio
import pyttsx3
from vosk import Model, KaldiRecognizer

# Constants
VOSK_MODEL_PATH = "models/vosk-model-small-en-us"
OLLAMA_API_URL = "http://localhost:11434/api/generate"
SAMPLE_RATE = 16000
BUFFER_SIZE = 4096


def load_sst_model():
    """
    Loads the Vosk speech recognition model.
    """
    if not os.path.exists(VOSK_MODEL_PATH):
        raise FileNotFoundError(
            "Vosk model not found! Place it in the 'models' directory."
        )
    return Model(VOSK_MODEL_PATH)


def convert_speech_to_text(model):
    """
    Captures audio from the microphone and transcribes it using Vosk.
    """
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=BUFFER_SIZE * 2,  # Double the buffer size
    )
    stream.start_stream()

    print("Listening... Speak now.")

    while True:
        data = stream.read(BUFFER_SIZE)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                return text


def process_query(input_text):
    """
    Sends the transcribed text to Ollama API and retrieves a response.
    """
    payload = {"model": "llama2:latest", "prompt": input_text}
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        response.raise_for_status()

        full_response = ""

        for line in response.iter_lines(decode_unicode=True):
            if line:
                data = json.loads(line)
                full_response += data.get("response", "")
                if data.get("done", False):
                    break

        return full_response or "No response generated."
    except requests.RequestException as e:
        return f"Error contacting Ollama API: {e}"


def convert_text_to_speech(text):
    """
    Converts text to speech and plays it.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    """
    Integrates speech recognition, AI processing, and text-to-speech.
    """
    try:
        model = load_sst_model()

        while True:
            user_input = convert_speech_to_text(model)
            print(f"User: {user_input}")

            response = process_query(user_input)
            print(f"Agent: {response}")

            convert_text_to_speech(response)

    except KeyboardInterrupt:
        print("\nExiting. Bye!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
