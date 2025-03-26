# Multilingual Assistant 

This Streamlit-based application allows you to interact with a multilingual AI assistant powered by Google Gemini Pro. You can communicate with the assistant through voice commands (using speech recognition) and receive responses in both text and spoken form.

## Features
 * Voice Input: Speak naturally to the assistant using your microphone.
 * Text Generation: The assistant leverages Google Gemini Pro to generate intelligent and contextually relevant responses.
 * Text-to-Speech: Hear the assistant's responses in a natural voice.
 * Download Speech: Download the assistant's responses as MP3 audio files.
   
## Requirements
* Python 3.7 or higher
* A Google Cloud API key with access to the Gemini Pro model
* The following Python libraries (specified in `requirements.txt`):
  * SpeechRecognition
  * pipwin
  * pyaudio
  * gTTS
  * google-generativeai
  * python-dotenv
  * streamlit



# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.11 -y
```

```bash
conda activate llmapp
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
streamlit run app.py
```

#### Add your GOOGLE_CLOUD_API_KEY credentials in  the Streamlit app. Get your [GOOGLE_CLOUD_API_KEY here](https://ai.google.dev/gemini-api): 

```ini
GOOGLE_CLOUD_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```



### Techstack Used:

- Python
- Google API
- Streamlit
- Gemini-pro
- s2t
- t2s


