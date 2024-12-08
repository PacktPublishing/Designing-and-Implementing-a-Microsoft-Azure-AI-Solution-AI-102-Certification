import os
from datetime import datetime

#Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound
from dotenv import load_dotenv

def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = os.getenv('SPEECH_REGION')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(subscription=ai_key, region=ai_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command and command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    print('Speak now...')

    # Process speech input
    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = result.text
        print(command)
    else:
        print(result.reason)
        if result.reason == speech_sdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    return command

def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour, now.minute)

    # Save the response as an audio file
    audio_filename = 'time.wav'
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    result = speech_synthesizer.speak_text_async(response_text).get()

    if result.reason == speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(response_text))
        # Play the audio file
        if os.path.isfile(audio_filename):
            # Use a short path to avoid the 8.3 filename convention issue
            short_path = os.path.abspath(audio_filename)
            playsound(short_path)
        else:
            print(f"Error: The file {audio_filename} does not exist.")
    else:
        print("Speech synthesis canceled, reason: {}".format(result.reason))
        if result.reason == speech_sdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print("Error details: {}".format(cancellation.error_details))

if __name__ == "__main__":
    main()