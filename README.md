# Audio to Text Sentiment Analysis with Speech Output

## Project Title
Audio to Text Sentiment Analysis and Text to Audio Conversion using Whisper and gTTS

## Introduction
This project is developed to build an automated audio processing system that converts spoken content into text, performs sentiment analysis on the extracted text, and generates a final spoken response. The main goal of this project is to combine Speech Processing and Natural Language Processing into a single workflow. The system accepts an audio file as input and produces both textual and audio output.

## Objective
The objective of this project is to:
- Convert audio into readable text
- Analyze sentiment from extracted text
- Identify whether the sentiment is positive or negative
- Generate a confidence score
- Convert final result into speech output

## Workflow
Audio Input → Speech Recognition → Text Generation → Sentiment Analysis → Positive or Negative Prediction → Text-to-Speech Conversion → Audio Output

## Features
- Upload audio files
- Convert speech into text
- Perform sentiment analysis
- Classify sentiment
- Display confidence score
- Convert response into speech
- Generate final audio output

## Technologies Used
Programming Language: Python
Libraries: Transformers, Torch, Librosa, gTTS
Models: Whisper, Sentiment Analysis Model
Platform: Google Colab

## System Architecture
Audio File → Whisper Model → Text Output → Sentiment Model → Result Processing → gTTS → Final Audio

## Module Description
Audio Upload Module: Allows users to upload audio files.
Speech Recognition Module: Uses Whisper to extract speech.
Sentiment Analysis Module: Analyzes emotions from extracted text.
Output Generation Module: Converts result into audio.

## Installation
Install dependencies:
``bash
pip install transformers torch librosa gtts
Execution Procedure
Open Google Colab.
Install required libraries.
Upload audio file.
Run Whisper model.
Extract text.
Perform sentiment analysis.
Generate final audio output.
Input

Supported Formats:

MP3
WAV

Example:
How are you.mp3

Output

Generated Outputs:

Recognized Text
Sentiment Result
Confidence Value
Final Audio
Example

Audio: Hello I am happy today
↓
Text: Hello I am happy today
↓
Sentiment: Positive
↓
Confidence: 0.98
↓
Audio Output Generated

Advantages
Fully automated
Fast processing
Easy implementation
Speech and NLP combined
User friendly
Limitations
Large models require more memory
Internet connection needed
Performance depends on audio quality
Future Enhancements
Multi-language support
Real-time microphone input
Web application deployment
Database integration
Improved sentiment prediction
Mobile support
Applications
Voice assistants
Customer feedback analysis
Accessibility tools
Education systems
Speech analytics
Conclusion

This project demonstrates an end-to-end pipeline for converting speech into meaningful information. It integrates speech recognition, sentiment classification, and speech generation into a complete intelligent system. The project can be extended for advanced AI applications.

References
Hugging Face Documentation
Whisper Model Documentation
Transformers Library
Python Documentation
gTTS Documentation
