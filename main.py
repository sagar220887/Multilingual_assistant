import streamlit as st
from src.helper import *


def main():
    st.subheader('Multilingual AI Assistant', divider='rainbow')

    if st.button('Ask me'):
        with st.spinner('Listening ...') as spinner:
            text=voice_input()
            response=get_llm_model(text)
            text_to_speech(response)
            
            
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()
            
            
            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")



if __name__ == "__main__":
    main()