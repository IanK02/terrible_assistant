import wave
import pyaudio
from google.cloud import speech
import google.generativeai as genai
import keyboard
import time
import numpy as np

'''
This class translates the recorded audio into text
'''
class stt():
    def __init__(self) -> None:
        self.client = speech.SpeechClient()

    #Record a .wav file of your voice
    def _record_wav(self, file_name) -> None:
        chunk = 1600
        format = pyaudio.paInt16
        channels = 1
        rate = 44100
        gain = 5.0
        with wave.open(file_name, 'wb') as wf:
            p = pyaudio.PyAudio()
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format))
            wf.setframerate(rate)

            stream = p.open(format=format, channels=channels, rate=rate, input=True)

            print('press r to start recording')
            while True:
                if keyboard.is_pressed('r'):
                    print('Recording...')
                    recording = True
                    time.sleep(0.5)
                    while recording:
                        data = stream.read(chunk, exception_on_overflow=False)
                        # Convert to numpy array
                        audio_data = np.frombuffer(data, dtype=np.int16)
                        # Apply mic gain
                        audio_data = audio_data * gain
                        # Clip to prevent overflow
                        audio_data = np.clip(audio_data, -32768, 32767).astype(np.int16)
                        # Write to file
                        wf.writeframes(audio_data.tobytes())
                        if keyboard.is_pressed('r'):
                            recording = False
                    print('Done')
                    stream.close()
                    p.terminate()
                    break
        
    #Transcribe the audio file of speech into text
    def _transcribe_file(self, file_name) -> str:
        """Transcribe the given audio file to text"""

        with open(file_name, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        #language_code can be changed to anything google has availabe on https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
        )

        response = self.client.recognize(config=config, audio=audio)
        #return the text content of the response
        return response.results[0].alternatives[0].transcript
    
    #method is not used, ask_gemini method in voiceai_test.py is used instead
    def _ask_gemini(self, query):
        genai.configure(api_key=os.getenv('API_KEY')
        model = genai.GenerativeModel('gemini-1.5-flash')
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=150,
        )
        response = model.generate_content(query, generation_config=generation_config)
        return response.text
    
    #main method used to record question and return the text content of the question
    def record_question(self) -> str:
        self._record_wav('your_question.wav')
        query = self._transcribe_file('your_question.wav')
        return query


