import os
import google.auth
from google.cloud import texttospeech

class VoiceGenerator:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def text_to_speech(self, text, output_file):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Build the voice request, select the language code and the ssml voice gender
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
        )

        # Perform the text-to-speech request
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Write the response to the output file
        with open(output_file, "wb") as out:
            out.write(response.audio_content)
            print(f"Audio content written to file {output_file}")

if __name__ == '__main__':
    generator = VoiceGenerator()
    generator.text_to_speech("Hello, world!", "output.mp3")