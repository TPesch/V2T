# V2T
Voice to Text Project

## Overview
The V2T project is designed to convert voice recordings into text transcriptions and translate them between English and German. The project includes various scripts for recording audio, transcribing it using the Whisper model, detecting the language, and translating the text.

## Installation
To use the code in this project, you need to install the following dependencies:

1. Python 3.8 or higher
2. Whisper
3. Langdetect
4. Googletrans
5. Sounddevice
6. Scipy
7. Keyboard
8. Numpy

You can install the required libraries using pip:

```sh
pip install whisper langdetect googletrans==4.0.0-rc1 sounddevice scipy keyboard numpy
```
## Project Structure
The project is organized into the following folders:

### 1. `Raw_Data`
This folder contains the raw audio data and text files used for training and testing the machine learning models.

### 2. `Live_Translations`
This folder is used to store the live transcriptions and translations generated during a session. Each session will have its own subfolder containing the audio recordings, transcriptions, and translations.

### 3. `Batch_Testing_Ai`
This folder contains scripts and data for batch testing the transcription and translation efficiency. It includes sample audio files and the corresponding translated text files.

### 4. `Final_code`
This folder contains the final versions of the scripts used for recording, transcribing, and translating audio. The main script in this folder is `Push_to_translate.py`.

### 5. `tests`
This folder is used for testing the machine learning code. It contains test scripts and sample data for verifying the functionality of the project.

## Usage
### Recording and Transcribing Audio
To record and transcribe audio, run the `Push_to_translate.py` script in the `Final_code` folder. The script will prompt you to enter a session name and then wait for you to press the spacebar to start recording. Press 's' to stop recording. The script will transcribe the audio and save the transcription and translation in the corresponding session folder.

### Batch Transcription and Translation
To perform batch transcription and translation, run the `Batch_Transcribe&Translate_efficiency_test.py` script in the `Batch_Testing_Ai` folder. The script will process all the sample audio files in the input folder, transcribe them, and save the translated text in the output folder.

## Example
Here is an example of how to use the `Push_to_translate.py` script:

```sh
python [Push_to_translate.py](http://_vscodecontentref_/0)
```
Follow the prompts to start and stop recording. The transcriptions and translations will be saved in the Live_Translations folder under the specified session name.
