import speech_recognition as sr

# Function to generate subtitles from audio file

def generate_subtitles(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio."  

# Example usage (commented out for user testing)
# subtitles = generate_subtitles('path_to_audio_file.wav')
# print(subtitles)