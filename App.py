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



# # Google API Key Setup
# GOOGLE_API_KEY = "AIzaSyCPFSXwMU3FBIBCk0FQ14ayQ62eoTqclgo"
# os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

# # Initialize the model once
# try:
#     model = llm_model_object(GOOGLE_API_KEY)
# except Exception as e:
#     st.error(f"Failed to initialize the model: {e}")

# # Function to get a response from the model with a timeout to avoid long waits
# def get_response(user_text, timeout=10):
#     try:
#         response = model.generate_content(user_text, timeout=timeout)  # Add a timeout to handle long response times
#         result = response.text
#         return result
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Main function for the Streamlit app
# def main():
#     st.title("Satheesh AI Assistant")

#     # Option to type the query
#     user_query = st.text_input("Type your query:", "")

#     # Option to ask a query via voice input
#     if st.button("Ask me anything!"):
#         with st.spinner("Listening..."):
#             try:
#                 text = voice_input()  # Capturing voice input
#                 response = llm_model_object(text)
#                 text_to_speech(response)
                
#                 # Display audio player and download link
                
#                 # Display audio player and download link
#                 audio_file = open("speech.mp3", 'rb')
#                 audio_bytes = audio_file.read()
#                 st.text_area(label="Response:", value=response, height=350)
#                 st.audio(audio_bytes, format='audio/mp3')
#                 st.download_button(label="Download Speech",
#                                 data=audio_bytes,
#                                 file_name="speech.mp3",
#                                 mime="audio/mp3")
#                 # if text:
#                 #     st.write("You asked:", text)
#                 #     response = get_response(text)
#                 #     st.write("Response:", response)
#                 #     audio = gTTS(response, lang='en')
#                 #     audio.save("response.mp3")
#                 #     st.audio("response.mp3", format="audio/mp3")
#             except sr.UnknownValueError:
#                 st.error("Could not understand audio. Please try again.")
#             except sr.RequestError as e:
#                 st.error(f"Could not request results from Google Speech Recognition service; {e}")
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")

#     # Option to handle typed query
#     if user_query:
#         st.write("You asked:", user_query)
#         response = get_response(user_query)
#         st.write("Response:", response)
#         try:
#             audio = gTTS(response, lang='en')
#             audio.save("response.mp3")
#             st.audio("response.mp3", format="audio/mp3")
#         except Exception as e:
#             st.error(f"Error generating audio: {e}")

#     # Add exit button to stop the running server
#     if st.button("Exit"):
#         st.write("Exiting the application...")
#         # Stop the Streamlit server
#         st.stop()

if __name__ == '__main__':
    main()
