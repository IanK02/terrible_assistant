import stt
import google.generativeai as genai
import tts
import os
import pygame
from pydub import AudioSegment

#Used to ask google gemini ai your question
def _ask_gemini(query):
        key = os.getenv('API_KEY')
        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        generation_config = genai.types.GenerationConfig(
            max_output_tokens=100,
        )
        #Prime the gemini ai response with a personality
        response_primer = """You are a massive conspiracy theorist who believes that the government is behind
        everything. Everything is the fault of big government and nothing and no one is to be trusted. You are extremely
        skeptical of anything asked of you or told to you. You have your own conspiracy theory for everything and love to share
        you theories with others"""
        full_prompt = f"{response_primer}\n\nHuman: {query}\n\nTheorist:"
        response = model.generate_content(full_prompt, generation_config=generation_config)
        return response.text

#Plays back the response from gemini ai
def _play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

#Used to boost the volume of the response, not needed when running on my computer but might
#be needed when running on Raspberry Pi
def _boost_volume(file_path):
     audio = AudioSegment.from_file(file_path)
     #audio = audio + 15    increase volume by 15dB, might be needed on RPi
     audio.export('response.wav', 'wav')

#Main method to record a user's question and read aloud gemini ai's response
def main():
    listener = stt.stt()
    writer = tts.text_to_speech('en-us', 'en-US-Neural2-I')
    gemini_prompt = listener.record_question()
    gemini_response = _ask_gemini(gemini_prompt)
    writer.read_aloud(gemini_response)
    #_boost_volume('response.wav')
    _play_sound('response.wav')

if __name__ == '__main__':
    main()


    