import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    st.title("Multilingual AI Assistant 🤖")

    # Input field for API key
    api_key = st.text_input("Enter your Google Cloud API Key:", type="password")

    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            if text:
                try:
                    response = llm_model_object(text)
                    text_to_speech(response)

                    audio_file = open("speech.mp3", "rb")
                    audio_bytes = audio_file.read()

                    st.text_area(label="Response:", value=response, height=350)
                    st.audio(audio_bytes)
                    st.download_button(label="Download Speech",
                                       data=audio_bytes,
                                       file_name="speech.mp3",
                                       mime="audio/mp3")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
            else:
                st.error("No speech detected. Please try again.")

if __name__ == '__main__':
    main()
