from google.cloud import texttospeech

'''
This class is used to translate the gemini ai reponse into speech using the google tts library
'''
class text_to_speech():
    def __init__(self, language: str, voice: str) -> None:
        #options for languages and voices can be found at https://cloud.google.com/text-to-speech/docs/voices
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code=language,
            name=voice,
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
            speaking_rate=1
        )

    #Uses google tts library to read aloud a given prompt and exports the audio to a .wav file
    def read_aloud(self, prompt: str):
        prompt_text = texttospeech.SynthesisInput(text=prompt)
        response = self.client.synthesize_speech(
            request={"input": prompt_text, "voice": self.voice, "audio_config": self.audio_config}
        )
        with open("response.wav", "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "response.wav"')

