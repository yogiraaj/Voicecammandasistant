# Personal Voice Assistant

A **Personal Voice Assistant** application built using Python, PyQt5, Speech Recognition Libraries, Natural Language Processing (NLP), and Machine Learning. This project allows hands-free user interaction, enabling quick access to information and automation of tasks through voice commands.

## Features

- Voice-activated commands for hands-free interaction
- Real-time speech recognition and conversion to text
- Natural Language Processing (NLP) for interpreting user queries
- Task automation: open applications, check the weather, search the web, and more
- Customizable responses using machine learning algorithms
- User-friendly interface created using PyQt5

## Technologies Used

- **Python**: Core programming language
- **PyQt5**: Used for GUI (Graphical User Interface)
- **Speech Recognition Libraries**: Converts voice input to text
  - `speech_recognition`, `pyaudio`
- **Natural Language Processing (NLP)**: Processes the user's spoken commands
  - `nltk`, `spacy`
- **Machine Learning**: Powers custom responses
- **Other Libraries**: 
  - `pyttsx3` for text-to-speech conversion
  - `smtplib` for sending emails through voice commands
  - `requests` for accessing APIs

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yogiraaj/voicecammandassistant.git
   cd voicecammandassistant

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Download required NLP models: If you're using nltk or spacy, make sure you download the necessary datasets:**
   ```bash
   python -m spacy download en_core_web_sm

## Usage
1. **Run the Application**
    ```bash
    python main.py

## Voice Cammands
The assistant can perform various tasks based on voice commands, such as: Mention in the main.py file.

## Customization
You can customize the assistant’s responses by tweaking the machine learning model or adding more NLP rules in the backend.

## GUI Overview
The assistant comes with a simple and intuitive user interface built using PyQt5. You can interact with the voice assistant through the GUI, which also displays the recognized text and assistant responses in real-time.

## Future Improvements
- Integration with IoT devices for home automation
- Support for more languages and regional accents
- Implementing deep learning techniques for more accurate voice recognition


This `README.md` provides:

- Clear instructions for installing dependencies
- Steps for downloading NLP models
- Optional environment setup
- Application usage instructions
- Customization details
- Overview of the graphical interface and future improvements





