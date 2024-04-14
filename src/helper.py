import speech_recognition as sr
import google.generativeai as genai

from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print('Could not understand the audio source')
        return None
    except sr.RequestError as e:
        print('Exception  - ', e)
        return None

def get_llm_model(user_query):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_query)
    result = response.text
    return result

    

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")