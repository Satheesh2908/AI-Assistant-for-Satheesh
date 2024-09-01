import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
from src.Helper import voice_input, text_to_speech, llm_model_object  # Ensure these imports are correct


def main():
    st.title("Satheesh AI Assistant")
    
    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)
            
            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")
# Add exit button to stop the running server
    if st.button("Exit"):
        st.write("Exiting the application...")
 # Stop the Streamlit server
        st.stop()

if __name__ == '__main__':
    main()
