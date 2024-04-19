
# import speech_recognition as sr

# AUDIO_FILE = ("your_file.wav")
# #use audio file as source

# r = sr.Recognizer() #initialize the recognizer

# with sr.AudioFile(AUDIO_FILE) as source:
    
#     audio = r.record(source)
#     #reads the audio file
    
# try:
#     print("Audio file contains " + r.recognize_google(audio))
    
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
    
# except sr.RequestError:
#     print("couldn't get the results from Google Speech Recognition")






import speech_recognition as sr

AUDIO_FILE = "path_to_your_audio_file.wav"  # Replace this with the actual path to your audio file
GOOGLE_API_KEY = "your_google_api_key"  # Replace this with your actual Google Speech Recognition API key

# Initialize the recognizer
r = sr.Recognizer()

# Use audio file as source
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # Reads the audio file

try:
    # Recognize speech using Google Speech Recognition
    print("Transcription: " + r.recognize_google(audio, key=GOOGLE_API_KEY))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


