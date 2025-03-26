import speech_recognition as sr  # type: ignore
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv  # type: ignore
import os
from gtts import gTTS  # type: ignore

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
        return ""
    except sr.RequestError as e:
        print(
            f"Could not request result from Google Speech Recognition service: {e}")
        return ""


def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")


def llm_model_object(user_text):
    if not GOOGLE_API_KEY:
        raise ValueError(
            "Google API Key is not set. Please check your .env file.")

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-pro")

    try:
        response = model.generate_content(user_text)
        result = response.text
        return result
    except Exception as e:
        print(f"An error occurred while generating content: {e}")
        return "I'm sorry, but I encountered an error while processing your request."


print("Helper module loaded successfully!")
